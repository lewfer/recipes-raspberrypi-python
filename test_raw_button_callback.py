# =====================================================================================================
# test_raw_button_callback.py
#
# This example uses raw GPIO calls to implement button functionality.
# For illustrating GPIO concepts only.  If you want to add a button to your project, it's easier to
# just use the gpiozero library (see test_button_callback.py).
# =====================================================================================================

import RPi.GPIO as GPIO
from time import sleep

# =====================================================================================================
# RawButtonPulldown class
# RawButtonPulldown: Connect the button to the pin and 3.3V.  Pin reads 0 when button not pressed and
# 1 when button pressed.
# =====================================================================================================

class RawButtonPulldown():

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)                                      # use BCM numbering
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # set the pin to input mode and pull down (button connected to pin and 3.3V)

    def value(self):
        return GPIO.input(self.pin)
        
    def pressed(self):
        return GPIO.input(self.pin)==1

    def event(self, callbackfn, rising=False):
        if rising:
            GPIO.add_event_detect(self.pin, GPIO.RISING, callback=callbackfn, bouncetime=200)   # event triggered when finger lifted off button
        else:
            GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=callbackfn, bouncetime=200)  # event triggered when finger pressed on button


# =====================================================================================================
# Main program
# =====================================================================================================

# Set up a callback function.  This will be run when a button is pressed
def callback(button):
    print("Called", button)

# Associate the Python RawButtonPulldown objects with the physical pins
b1 = RawButtonPulldown(13) # connect button to pin 13 and +3.3V
b2 = RawButtonPulldown(19) # connect button to pin 19 and +3.3V

# Associate the button objects with the callback function
print("Waiting for callback")
b1.event(callback)
b2.event(callback)

# Wait for a button to be pressed
while True:
    sleep(0.1)

GPIO.cleanup()