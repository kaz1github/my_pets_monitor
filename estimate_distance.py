import RPi.GPIO as GPIO
import time
 
trigger_pin = 23
echo_pin = 24
 
class EstimateDistance:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)

    def send_trigger_pulse(self):
        GPIO.output(trigger_pin, True)
        time.sleep(0.0001)
        GPIO.output(trigger_pin, False)
 
    def wait_for_echo(self, value, timeout):
        count = timeout
        while GPIO.input(echo_pin) != value and count > 0:
            count = count - 1
 
    def get_distance(self):
        self.send_trigger_pulse()
        self.wait_for_echo(True, 10000)
        start = time.time()
        self.wait_for_echo(False, 10000)
        finish = time.time()
        pulse_len = finish - start
        distance_cm = pulse_len / 0.000058
        distance_in = distance_cm / 2.5
        return (distance_cm, distance_in)
        GPIO.cleanup()

if __name__ == '__main__':
    ins = EstimateDistance()
    while True:
        cm,disin = ins.get_distance()
        print("{:.2f}cm".format(cm))
        time.sleep(1)
