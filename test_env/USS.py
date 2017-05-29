import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

TRIG_voor = 23                                  #Associate pin 23 to TRIG
ECHO_voor = 24                                  #Associate pin 24 to ECHO

TRIG_achter = 06                                  #Associate pin 05 to TRIG
ECHO_achter = 05                                  #Associate pin 06 to ECHO

print "Distance measurement in progress"

GPIO.setup(TRIG_voor,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO_voor,GPIO.IN)                   #Set pin as GPIO in

GPIO.setup(TRIG_achter,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO_achter,GPIO.IN)                   #Set pin as GPIO in

while True:

  GPIO.output(TRIG_voor, False)                 #Set TRIG as LOW
  GPIO.output(TRIG_achter, False)
  
  print "Waitng For Sensor To Settle"
  time.sleep(0.2)                            #Delay of 2 seconds

  #####################################################################

  GPIO.output(TRIG_voor, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG_voor, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO_voor)==0:               #Check whether the ECHO is LOW
    pulse_start_voor = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO_voor)==1:               #Check whether the ECHO is HIGH
    pulse_end_voor = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration_voor = pulse_end_voor - pulse_start_voor #Get pulse duration to a variable

  distance_voor = pulse_duration_voor * 17150        #Multiply pulse duration by 17150 to get distance
  distance_voor = round(distance_voor, 2)            #Round to two decimal points


  #####################################################################

  GPIO.output(TRIG_achter, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG_achter, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO_achter)==0:               #Check whether the ECHO is LOW
    pulse_start_achter = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO_achter)==1:               #Check whether the ECHO is HIGH
    pulse_end_achter = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration_achter = pulse_end_achter - pulse_start_achter #Get pulse duration to a variable

  distance_achter = pulse_duration_achter * 17150        #Multiply pulse duration by 17150 to get distance
  distance_achter = round(distance_achter, 2)            #Round to two decimal points

  #####################################################################

  if distance_voor > 2 and distance_voor < 400:      #Check whether the distance is within range
    print "Distance voor:",distance_voor - 0.5,"cm"  #Print distance with 0.5 cm calibration
  else:
    print "Voor Out Of Range"                   #display out of range


  if distance_achter > 2 and distance_achter < 400:      #Check whether the distance is within range
    print "Distance achter:",distance_achter - 0.5,"cm"  #Print distance with 0.5 cm calibration
  else:
    print "achter Out Of Range"                   #display out of range
