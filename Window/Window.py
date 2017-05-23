from Tkinter import *

class test:
	
	def __init__(self, master):
			self.Snelheid = 0
			frame = Frame(master)
			frame.pack()
			self.button = Button(frame,
								 text="Accelerate", fg="green",
								 command=self.Versnel)
			self.button.pack(side=LEFT)
	def Versnel(self):
		self.Snelheid = self.Snelheid + 25 
		print(self.Snelheid)


root = Tk()
app = test(root)
root.mainloop()
