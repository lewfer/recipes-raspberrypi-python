# =====================================================================================================
# test_raw_photocell.py
#
# This example uses raw GPIO calls to drive a photocell.
# For illustrating GPIO concepts only.  If you want to add a photocell to your project, it's easier to
# just use the gpiozero library (see test_photocell.py).
# =====================================================================================================

import RPi.GPIO as GPIO
from time import sleep

# ======================================================================================================
# Photocell class
# ======================================================================================================

class Photocell():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)                   # use BCM numbering
    
    def __del__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup(self.pin)

    def read(self):
        # Start a counter
        count = 0
    
        # Start with the pin low
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
        sleep(0.1)

        # Change the pin to input mode
        GPIO.setup(self.pin, GPIO.IN)
    
        # Keep counting until the pin goes high
        while (GPIO.input(self.pin) == GPIO.LOW):
            count += 1

        # Return the count
        return count 

# ======================================================================================================
# Main program
# =====================================================================================================

p = Photocell(26)

while True:
    print (p.read())
    sleep(0.1)
