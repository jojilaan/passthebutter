# import libraries
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)        # pin 16 for PWM
GPIO.setup(20, GPIO.OUT)        # pin 20 for Direction
GPIO.output(20, GPIO.HIGH)      # or GPIO.LOW
pwm = GPIO.PWM(16, 100)
pwm.start(1)                    # Duty Cycle of 1

for i in range(0, 100):         # Loop for 10 seconds
    pwm.ChangeDutyCycle(100)    # Make the Rover Motors go full speed
    time.sleep(.1)

pwm.stop()
pwm.cleanup()
