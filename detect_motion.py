import RPi.GPIO as GPIO
import time
INTAVAL = 3
SLEEPTIME = 1
SENSOR_PIN = 4

class DetectMotion: 
    def __init__(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SENSOR_PIN, GPIO.IN)        

    def detecting(self):
        self.flg = False
        st = time.time()-INTAVAL
        print(GPIO.input(SENSOR_PIN))
        if(GPIO.input(SENSOR_PIN) == GPIO.HIGH) and (st + INTAVAL < time.time()):
            st = time.time()
            print("感知しました。")
            self.flg = True
        time.sleep(SLEEPTIME)
        return self.flg

if __name__ == '__main__':
    ins = DetectMotion()
    while True:
        ins.detecting()
