'''
1 Yellow 5
2 Blue 3
3 White 8
Sequence : 1 , 2 , 3 , 2 , 1 
'''
from time import sleep
import RPi.GPIO as GPIO

def blink(pin):
	GPIO.output(pin,1)
	print "On"
	sleep(1)
	GPIO.output(pin,0)
	print "Off"
	sleep(1)

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

pins_list = [5,3,8]

for pin in pins_list:
	GPIO.setup(pin,GPIO.OUT)	
                                                                                                                                                
n=0
while True:
	pin=pins_list[n%3]
	n=n+1
	blink(pin)