import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
pwm = GPIO.PWM(16, 100)
pwm.start(5)

for i in range(0, 100):
    pwm.ChangeDutyCycle(100)
    time.sleep(.1)

pwm.stop(pin)
pwm.cleanup()
