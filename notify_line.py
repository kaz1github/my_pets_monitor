import requests
from settings import Settings
import traceback

class NotifyLine:
    def __init__(self):
        self.url = Settings.LINE_URL
        self.token = Settings.LINE_TOKEN
        self.headers = {"Authorization" : "Bearer "+ self.token}
        

    def send_message(self):
        self.message =  "トイレするようです。\n様子を見る場合ははこちら：" + Settings.STREAM_ADDRESS
        self.payload = {"message" :  self.message}
        # self.files = {"imageFile": open(img_file, "rb")}
        # バイナリで画像ファイルを開く。対応形式PNG/JPEG
        try:
            # result = requests.post(self.url, headers = self.headers ,params = self.payload, files = self.files)
            result = requests.post(self.url, headers = self.headers ,params = self.payload)
        except:
            print("Error : 送信できませんでした。")
            print("===== エラー内容 =====")
            traceback.print_exc()

if __name__ == '__main__':
    ins = NotifyLine()
    ins.send_message("./test.jpg")
