import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)                   # use BCM numbering
GPIO.setup(21, GPIO.OUT)           # set the pin to output mode

GPIO.output(21,GPIO.HIGH)
sleep(2)
GPIO.output(21,GPIO.LOW)

GPIO.cleanup()
