import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os
from settings import Settings
import traceback

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

jp='iso-2022-jp'

class SendEmail:
    def __init__(self):
        self.gmail_user = Settings.MAIL_USER
        self.gmail_pass = Settings.MAIL_PW
        self.address_from = Settings.MAIL_ADDRESS
        self.address_to = Settings.MAIL_ADDRESS

    def send_email(self):
        try:
            smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
        except:
            print("サーバーに接続できませんでした。")
            print("===== エラー内容 =====")
            traceback.print_exc()
        try:
            smtpserver.login(self.gmail_user, self.gmail_pass)
        except:
            print("Emailにログインできませんでした。")
            print("===== エラー内容 =====")
            traceback.print_exc()

        self.subject  = "トイレのお知らせ"
        self.text = "トイレをするようです。\n様子を見る場合はこちら：" + Settings.STREAM_ADDRESS
        # inputメソッドでは改行コードが無視されるので改行コードを含む場合に変換する。 
        if self.text.find('¥n') > -1:
            self.text = self.text.replace('¥n', os.linesep)

        self.msg = MIMEMultipart()
        self.msg['Subject'] = self.subject
        self.msg['From'] = self.address_from
        self.msg['To'] = self.address_to
        self.body_text = self.text
        self.msg.attach(MIMEText(self.body_text, 'plain', 'utf-8'))
        smtpserver.sendmail(self.gmail_user, self.address_to, self.msg.as_string())

        smtpserver.close()

if __name__ == '__main__':
    ins = SendEmail()
    ins.send_email()
