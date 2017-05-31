import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

for x in range (0, 3000000):
    GPIO.output(21, True)
    time.sleep(0.000008)
    GPIO.output(21, False)
    time.sleep(0.000008)
