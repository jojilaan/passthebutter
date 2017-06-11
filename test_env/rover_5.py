# import libraries
import RPi.GPIO as GPIO
import time

# pin 16 for PWM signal
# pin 20 for Direction signal

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.output(20, GPIO.HIGH)      # or GPIO.LOW
pwm = GPIO.PWM(16, 100)
pwm.start(1)                    # Duty Cycle of 1

for i in range(0, 100):
    pwm.ChangeDutyCycle(100)    # Make the Rover Motors go full speed
    time.sleep(.1)
#run for 10 sec.

pwm.stop()
pwm.cleanup()
