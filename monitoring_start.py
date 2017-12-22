from capture_image import *
from detect_motion import *
from estimate_distance import *
from notify_line import *
from send_email import *
from give_alert import *
import math
import time

CAPTURE_INTERVAL = 20
INITIAL_INTERVAL = 5
INTERVAL = 300
CAPTURE_TIMES = 3

cap_img = CaptureImage()
notification = NotifyLine()
email = SendEmail()
detect = DetectMotion()
estimate = EstimateDistance()
alert = GiveAlert()
capture_time = time.time() -300

while True:
    set_time = time.time()
    if (detect.detecting() == True) and (set_time > capture_time + INTERVAL):
        notification.send_message()
        email.send_email()
        for i in range(CAPTURE_TIMES):
            if i == 0: time.sleep(INITIAL_INTERVAL)
            cap_img.save_image()
            if i != 2: time.sleep(CAPTURE_INTERVAL)
        capture_time = time.time()
    cm, b = estimate.get_distance()
    if cm < 20:
        alert.buzz()
        print("{:.2f}cm".format(cm))
        
