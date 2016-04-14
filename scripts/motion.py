import logging
import time
import RPi.GPIO as io
io.setmode(io.BCM)


door_pin = 16 #set door pin
sensorTrigger = True #set trigger flag

##create logger##

logger = logging.getLogger('doorhub')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('doorhub.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s- %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

##setup io pin##
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)

def door_open():
	logger.info('DOOR OPENED')

def door_close():
	logger.info('DOOR CLOSED')

while True:
	if io.input(door_pin):
	  if (sensorTrigger):
		#print("DOOR OPENED")
		door_open()
		sensorTrigger = False #to prevent multi time trigger
		time.sleep(1)
	if not io.input(door_pin):
	  if not (sensorTrigger):
		#print("DOOR CLOSED")
		door_close()
		sensorTrigger = True #to prevent multi time trigger
		time.sleep(1)
