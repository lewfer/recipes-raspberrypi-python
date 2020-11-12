import RPi.GPIO as GPIO

# ======================================================================================================
# MotorL293D class
# ======================================================================================================

class MotorL293D():
    def __init__(self, enablePin, forwardPin, backwardPin):
        GPIO.setmode(GPIO.BCM)                                      # use BCM numbering
        self.enablePin = enablePin
        self.forwardPin = forwardPin
        self.backwardPin = backwardPin
        GPIO.setup(self.enablePin, GPIO.OUT)   
        GPIO.setup(self.forwardPin, GPIO.OUT)
        GPIO.setup(self.backwardPin, GPIO.OUT)

    def __del__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup([self.enablePin, self.forwardPin, self.backwardPin])

    def turnMotor(self, speed):
        # Set up PWM
        self.pwm1 = GPIO.PWM(self.enablePin, 100)                  # 100 dutycycle
        self.pwm1.start(0)                                         # start at 0 dutycycle

        GPIO.output(self.forwardPin, True if speed>0 else False)   # set forward pin on if moving forward
        GPIO.output(self.backwardPin, True if speed<0 else False)  # set backward pin on if moving backward
        self.pwm1.ChangeDutyCycle(abs(speed))                      # % speed indicated by duty cycle
        GPIO.output(self.enablePin, True)                          # start the motor spinning

    def stopMotor(self):   
        GPIO.output(self.enablePin, False)                         # stop the motor spinning
        self.pwm1.stop()        
      

