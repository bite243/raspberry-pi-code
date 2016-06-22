'''
LEDs

Blue positive=blue
	BOARD= 8
Yellow positive=yellow
	BOARD= 12 
Green positive=green
	BOARD= 18
All negatives=purple 
'''
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(8,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

def blink(pin):
	GPIO.output(pin,True)
	time.sleep(1)
	GPIO.output(pin,False)
	time.sleep(1)

def twoled(pin1,pin2):
	GPIO.output(pin1,True)
	time.sleep(1)
	GPIO.output(pin1,False)
	time.sleep(1)

	GPIO.output(pin2,True)
	time.sleep(1)
	GPIO.output(pin2,False)
	time.sleep(1)

def 
