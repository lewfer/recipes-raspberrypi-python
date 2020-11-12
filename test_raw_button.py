
# =====================================================================================================
# test_raw_button.py
#
# This example uses raw GPIO calls to implement button functionality.
# For illustrating GPIO concepts only.  If you want to add a button to your project, it's easier to
# just use the gpiozero library (see test_button.py).
# =====================================================================================================

import RPi.GPIO as GPIO
from time import sleep

# =====================================================================================================
# RawButtonPullup class
# RawButtonPullup: Connect the button to the pin and ground.  Pin reads 1 when button not pressed and
# 0 when button pressed.
# =====================================================================================================

class RawButtonPullup():

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)                                      # use BCM numbering
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # set the pin to input mode and pull up (button connected to pin and ground)

    def value(self):
        return GPIO.input(self.pin)

    def pressed(self):
        return GPIO.input(self.pin)==0

    def event(self, callbackfn, rising=False):
        if rising:
            GPIO.add_event_detect(self.pin, GPIO.RISING, callback=callbackfn, bouncetime=200)   # event triggered when finger lifted off button
        else:
            GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=callbackfn, bouncetime=200)  # event triggered when finger pressed on button


# ======================================================================================================
# Main program
# =====================================================================================================

# Associate the Python button RawButtonPullup with the physical pin
b1 = RawButtonPullup(13)    # connect button to pin 13 and GND

# Wait for a button to be pressed
while not b1.pressed():
    print ("Please press the button")
print("Thank you")
GPIO.cleanup()

