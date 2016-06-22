

# importing module(library) add new set of commmands to python
import time
# importing new module and nicknaming it 'GPIO'
import RPi.GPIO as GPIO
# setting the mode for pins, shows which side of label
GPIO.setmode(GPIO.BCM)
# setting the pinnumber as an input
GPIO.setup(14,GPIO.IN)

while True:
	read_input=GPIO.input(14)
	print (read_input)
	time.sleep(1)