import RPi.GPIO as GPIO

# ======================================================================================================
# MotorMD10C class
# ======================================================================================================

class MotorMD10C():
    def __init__(self, dirPin, pwmPin):
        GPIO.setmode(GPIO.BCM)                                      # use BCM numbering
        self.dirPin = dirPin
        self.pwmPin = pwmPin
        GPIO.setup(self.dirPin, GPIO.OUT)   
        GPIO.setup(self.pwmPin, GPIO.OUT)

        # Set up PWM
        self.pwm1 = GPIO.PWM(self.pwmPin, 1000)                    # frequency
        self.pwm1.start(0)                                         # start at 0 dutycycle

    def __del__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup([self.dirPin, self.pwmPin])

    def turnMotor(self, speed):

        GPIO.output(self.dirPin, True if speed>0 else False)       # set dir pin on if moving forward
        self.pwm1.ChangeDutyCycle(abs(speed))                      # % speed indicated by duty cycle

     