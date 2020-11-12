# =====================================================================================================
# test_raw_led.py
#
# This example uses raw GPIO calls to implement led functionality.
# For illustrating GPIO concepts only.  If you want to add an led to your project, it's easier to
# just use the gpiozero library (see test_led.py).
# =====================================================================================================

import RPi.GPIO as GPIO
from time import sleep

# =====================================================================================================
# RawLed class
# =====================================================================================================

class RawLed():

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)                   # use BCM numbering
        GPIO.setup(self.pin, GPIO.OUT)           # set the pin to output mode

    def on(self):
        GPIO.output(self.pin,GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin,GPIO.LOW)


# ======================================================================================================
# Main program
# =====================================================================================================

# Associate the Python RawLedPwm objects with the physical pin
led = RawLed(17)

# Turn led on and off
led.on()    
sleep(2)
led.off()
sleep(2)

# Clean up
GPIO.cleanup()
