import requests
from settings import Settings

class NotifyLine:
    def __init__(self):
        self.url = Settings.LINE_URL
        # self.url = "aaa"
        self.token = Settings.LINE_TOKEN
        self.headers = {"Authorization" : "Bearer "+ self.token}
        

    def send_message(self, img_file):
        self.message =  '感知しました。画像を送ります。' 
        self.payload = {"message" :  self.message}
        self.files = {"imageFile": open(img_file, "rb")}
        # バイナリで画像ファイルを開く。対応形式PNG/JPEG
        try:
            result = requests.post(self.url, headers = self.headers ,params = self.payload, files = self.files)
        except:
              print("Error : 送信できませんでした。")
              exit()

if __name__ == '__main__':
    ins = NotifyLine()
    ins.send_message("./test.jpg")
