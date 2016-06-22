'''
Use button to turn on a LED
'''

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(16,GPIO.OUT)
#input is BOARD 8 
#output is BOARD 16

while True: 
	input=GPIO.input(8)
	if input == 0:
		GPIO.output(16,True)
	if input == 1:
		GPIO.output(16,False)
	print(input)
	