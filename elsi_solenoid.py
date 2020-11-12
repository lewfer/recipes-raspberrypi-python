import RPi.GPIO as GPIO
from time import sleep

# ======================================================================================================
# SolenoidL9110S class
# ======================================================================================================

class SolenoidL9110S():
    def __init__(self, triggerPin, groundPin):
        GPIO.setmode(GPIO.BCM)                                      # use BCM numbering
        self.triggerPin = triggerPin
        self.groundPin = groundPin
        GPIO.setup(self.triggerPin, GPIO.OUT)
        GPIO.setup(self.groundPin, GPIO.OUT)

    def __del__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup(self.triggerPin)

    def fire(self, seconds=1):
        GPIO.output(self.triggerPin, True)
        GPIO.output(self.groundPin, False)
        sleep(seconds)
        GPIO.output(self.triggerPin, False)
        
