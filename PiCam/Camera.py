#i:mport the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
#initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.vflip = True
camera.resolution = (320,240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320,240))

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port = True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	#Start function for detecting object
	
	faces = faceCascade.detectMultiScale(
					image,
					scaleFactor=1.1,
					minNeighbors=5,
					minSize=(30, 30),
	)

	for (x, y, w, h) in faces:
			cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 255), 2)


	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)	
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
