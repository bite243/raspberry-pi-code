'''
Use for loop to blink led 10 times
Use while loop to have counter
	- If the counter reaches ten then it should stop
'''
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)

def blink(seconds):
	GPIO.output(14,True)
	print "light on"
	time.sleep(seconds)
	GPIO.output(14,False)
	print "light off"
	time.sleep(seconds)

switch = 0
while switch < 3:
	switch = switch+1	
	blink(0.5)
 
light = [1,2,3]
for test in light:
	blink(1)

print("End of Code")
'''
Put positive wire in output 
Put negative wire in ground(GND)
'''