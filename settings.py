import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Settings:
    MAIL_USER = os.environ.get("MAIL_USER")
    MAIL_PW = os.environ.get("MAIL_PW")
    MAIL_ADDRESS = os.environ.get("MAIL_ADDRESS")
    LINE_URL = os.environ.get("LINE_URL")
    LINE_TOKEN = os.environ.get("LINE_TOKEN")
    MONITOR_USER = os.environ.get("MONITOR_USER")
    MONITOR_PW = os.environ.get("MONITOR_PW")
    ADDRESS = os.environ.get("ADDRESS")
    STREAM_ADDRESS = os.environ.get("STREAM_ADDRESS")

if __name__ == '__main__':
    pass
