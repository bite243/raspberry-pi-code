'''
Use for loop to blink led 10 times
Use while loop to have counter
	- If the counter reaches ten then it should stop
'''

import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
switch = 0
 
while switch < 2:
	switch = switch+1	
	print(switch) 
	light = [1,2,3,4,5]
	for test in light:
		GPIO.output(14,True)
		print "light on"
		time.sleep(2)
		GPIO.output(14,False)
		print "light off"
		time.sleep(2)

'''
Put positive wire in output 
Put negative wire in ground(GND)
'''