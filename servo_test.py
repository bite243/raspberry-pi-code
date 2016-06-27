'''

'''

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
pwm_object = GPIO.PWM(8,50)

def move(pos):
	pwm_object.ChangeDutyCycle(pos)
	
while True: 
	pwm_object.start(7.5)
	time.sleep(1)
	move(12)
	time.sleep(1)
	move(3)
	
GPIO.cleanup()