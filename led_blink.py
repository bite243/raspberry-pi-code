'''
Use for loop to blink led 10 times
Use while loop to have counter
	- If the counter reaches ten then it should stop
'''
# importing module(library) add new set of commmands to python
import time
# importing new module and nicknaming it 'GPIO'
import RPi.GPIO as GPIO
# setting the mode for pins, shows which side of label
GPIO.setmode(GPIO.BCM)
# setting the pinnumber as an output
GPIO.setup(18,GPIO.OUT)
# Telling the out put to turn on
GPIO.output(18,True)
#delay
time.sleep(2)
#Turn off
GPIO.output(18,False)