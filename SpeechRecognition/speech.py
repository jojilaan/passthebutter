#import Libraries that are being used
import speech_recognition as sr
# https://github.com/Uberi/speech_recognition -> Examples -> microphone_recognition.py
# 15 may 2017

while (1==1):
#First make the microphone listen for speechfragments
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("What is my purpose?")
		audio = r.listen(source)

#now send it to Google to do some magic with it, and return it as a string
	try:
		print("I think you said the following phrase:\n" + r.recognize_google(audio))
	except sr.UnknownValueError:
		print("I could not understand what you were saying...")
	except sr.RequestError as e:
		print("The following error had occured from the Google Recognition Service: {0}".format(e))
