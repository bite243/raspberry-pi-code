'''
Use for loop to blink led 10 times
Use while loop to have counter
	- If the counter reaches ten then it should stop
'''
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)

def blink(times_list):
	print times_list[0:]	
	GPIO.output(14,True)
	time.sleep(times_list[0])
	print "light off"
	GPIO.output(14,False)
	time.sleep(times_list[1])

switch = 0
while switch < 3:
	switch = switch+1	
	blink([0.01,1]) 
light = [1,2,3]
for test in light:
	blink([1,0.01])

print("End of Code")
'''
Put positive wire in output 
Put negative wire in ground(GND)
'''