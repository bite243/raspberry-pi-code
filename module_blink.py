'''
This file should contain the function defenition for blinking an led
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

'''
Put positive wire in output 
Put negative wire in ground(GND)
'''