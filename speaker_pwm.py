import time
import RPi.GPIO as GPIO

pin=8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)
'''
write a loop that changes frequency
from 100 to 10,000 in increments of 500
'''

frequency=100
duty_cycle=10

while frequency < 10000:	
	pwm_object=GPIO.PWM(pin,frequency)
	frequency=frequency+500
	print (frequency)
	pwm_object.start(duty_cycle)
	while duty_cycle < 100:
		pwm_object.ChangeDutyCycle(duty_cycle)
		duty_cycle=duty_cycle+20
		print(duty_cycle)
		time.sleep(2)

GPIO.cleanup()