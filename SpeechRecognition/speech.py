#import library for speech recognition
import speech_recognition as sr

# This test code is based on the following code on github:
# https://github.com/Uberi/speech_recognition -> Examples -> microphone_recognition.py
# 15 may 2017

#Loop the Speech Recognition 
while (True):
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
	except sr.RequestError as e:        #if something went wrong...
		print("The following error had occured from the Google Recognition Service: {0}".format(e))
