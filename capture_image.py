import requests
import io
from PIL import Image
from datetime import datetime
from settings import Settings
import traceback

class CaptureImage:
    def __init__(self):
        self.url = "http://{}:8080".format(Settings.ADDRESS)
        self.payload = {"action": "snapshot"}
        self.auth_user = Settings.MONITOR_USER
        self.auth_password = Settings.MONITOR_PW

    def capture(self, timeout = 10):
        try:
            response = requests.get(self.url, params = self.payload, auth = (self.auth_user, self.auth_password), allow_redirects=False, timeout=timeout)
        except:
            print("リクエストに失敗しました。")
            print("===== エラー内容 =====")
            traceback.print_exc()
        if response.status_code != 200:
            e = Exception("HTTP status: " + response.status_code)
            raise e

        content_type = response.headers["content-type"]
        if 'image' not in content_type:
            e = Exception("Content-Type: " + content_type)
            raise e
        return response.content

    def save_image(self):
        res = self.capture()
        img = Image.open(io.BytesIO(res))
        cap_time = datetime.now().strftime("%Y%m%d%H%M%S")
        img.save("./flaskr/static/image/{}.jpg".format(str(cap_time)))

if __name__ == '__main__':
    ins = CaptureImage()
    ins.save_image()
