'''
Button Toggle/Switch Mode
'''
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO. BOARD)
GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,False)
led_status=0

while True:
	input=GPIO.input(8)
	if input < 1:
		sleep(0.2)
		if led_status==1:
			GPIO.output(3,False)
			led_status=0
			print "off"
		elif led_status==0:
			GPIO.output(3,True)
			led_status=1
			print "on"


'''
	input=GPIO.input(8)
	if input == 0:
		GPIO.output(3,True)
	if input == 1:
		GPIO.output(3,False)
	print(input)
'''