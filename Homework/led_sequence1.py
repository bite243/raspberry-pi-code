'''
1 Yellow 8
2 Green 3
3 White 7
'''
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

GPIO.output(18,True)
time.sleep(1)
GPIO.output(18,False)