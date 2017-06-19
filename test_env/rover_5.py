# import libraries
import RPi.GPIO as GPIO
import time
class Rover(object):
		
		def __init__(self, speed):
				self.speed = speed
				
				GPIO.setmode(GPIO.BCM)
				GPIO.setup(9, GPIO.OUT)					#Pwm LEFT        
				GPIO.setup(11, GPIO.OUT)				#Dir LEFT
				self.pwm_L = GPIO.PWM(9, 100)

				GPIO.setup(25, GPIO.OUT)				#Pwm Right        
				GPIO.setup(8, GPIO.OUT)					#Dir Right
				self.pwm_R = GPIO.PWM(25, 100)
				
				self.pwm_L.start(0)
				self.pwm_R.start(0)

		def goForward(self, speed):
				self.speed = speed
				GPIO.output(11, GPIO.HIGH)
				GPIO.output(8, GPIO.LOW)
				self.pwm_L.ChangeDutyCycle(self.speed)
				self.pwm_R.ChangeDutyCycle(self.speed)

		def goBackward(self, speed):
				self.speed = speed
				GPIO.output(11, GPIO.LOW)
				GPIO.output(8, GPIO.HIGH)
				self.pwm_L.ChangeDutyCycle(self.speed)
				self.pwm_R.ChangeDutyCycle(self.speed)

		def stopRover(self):
				self.speed = 0
				self.pwm_L.ChangeDutyCycle(0)
				self.pwm_R.ChangeDutyCycle(0)
		
		def goRight(self, speed):
				self.speed = speed
				GPIO.output(11, GPIO.HIGH)
				GPIO.output(8, GPIO.HIGH)
				self.pwm_L.ChangeDutyCycle(self.speed)
				self.pwm_R.ChangeDutyCycle(self.speed)

		def goLeft(self, speed):
				self.speed = speed
				GPIO.output(11, GPIO.LOW)
				GPIO.output(8, GPIO.LOW)
				self.pwm_L.ChangeDutyCycle(self.speed)
				self.pwm_R.ChangeDutyCycle(self.speed)

		def cleanUp(self):
				GPIO.cleanup(9)
				GPIO.cleanup(11)
				GPIO.cleanup(25)
				GPIO.cleanup(8)

'''
if __name__ == '__main__':
		rover = Rover(0)
		rover.goLeft(100)
		print("Going forward with 100% speed for 10 secs")
		time.sleep(10)
		rover.stopRover()
		print("Stopping rover for 1 sec")
		time.sleep(1)
		rover.goRight(100)
		time.sleep(10)
		rover.stopRover()
		rover.cleanUp()
'''
