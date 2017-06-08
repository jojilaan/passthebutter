# import libraries
import RPi.GPIO as GPIO
import time

'''
pin 16 voor voor-links
pin 20 voor achter-links


'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
pwm = GPIO.PWM(16, 100)
pwm.start(5)

for i in range(0, 100):
    pwm.ChangeDutyCycle(100)
    time.sleep(.1)
#run for 10 sec.

pwm.stop(pin)
pwm.cleanup()
