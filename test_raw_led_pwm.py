# =====================================================================================================
# test_raw_led_pwm.py
#
# This example uses raw GPIO calls to implement analogue led functionality.
# For illustrating GPIO concepts only.  If you want to add an led to your project, it's easier to
# just use the gpiozero library (see test_led_pwm.py).
# =====================================================================================================

import RPi.GPIO as GPIO
from time import sleep

# =====================================================================================================
# RawLedPwm class
# =====================================================================================================

class RawLedPwm():

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)                   # use BCM numbering
        GPIO.setup(self.pin, GPIO.OUT)           # set the pin to output mode
        self.pwm=GPIO.PWM(self.pin, 50)          # set up pin for PWM mode
        self.pwm.start(0)                        # start with led off
        self.value = 0

    def stop(self):       
        self.pwm.stop()

    def setValue(self, percentage):
        self.pwm.ChangeDutyCycle(percentage)


# ======================================================================================================
# Main program
# =====================================================================================================

# Associate the Python RawLedPwm objects with the physical pin
led = RawLedPwm(17)

# Increase the brightness of the led
for percentage in range(0,100,10):
    led.setValue(percentage / 100)
    sleep(2)

# Clean up
led.stop()
GPIO.cleanup()
