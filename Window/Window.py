from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)

class App:
	
	def __init__(self, master):
			self.Snelheid = 0
			frame = Frame(master)
			frame.pack()
			self.button = Button(frame,
                                                text="Accelerate", fg="green",
						command=self.Versnel)
			self.button.pack(side=RIGHT)

			self.button = Button(frame,
                                                text="Decelerate", fg="red",
						command=self.Vertraag)
			self.button.pack(side=LEFT)
			
	def Versnel(self):
		self.Snelheid = self.Snelheid + 10
		print(self.Snelheid)
		duty = float(self.Snelheid) / 10.0 + 2.5
                pwm.ChangeDutyCycle(duty)

	def Vertraag(self):
                self.Snelheid = self.Snelheid - 10
                print(self.Snelheid)
                duty = float(self.Snelheid) / 10.0 + 2.5
                pwm.ChangeDutyCycle(duty)


root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()
