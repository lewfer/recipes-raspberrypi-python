# =====================================================================================================
# test_raw_motor_l9110s.py
#
# This example uses raw GPIO calls to drive a motor.
# For illustrating GPIO concepts only.  If you want to add a motor to your project, it's easier to
# just use the gpiozero library (see test_motor_l9110s.py).
# =====================================================================================================

import RPi.GPIO as GPIO
from time import sleep

# ======================================================================================================
# RawMotorL9110S class
# ======================================================================================================

class RawMotorL9110S():
    def __init__(self, forwardPin, backwardPin):
        GPIO.setmode(GPIO.BCM)                                      # use BCM numbering
        self.pwmF = None
        self.pwmB = None
        self.forwardPin = forwardPin
        self.backwardPin = backwardPin
        GPIO.setup(self.forwardPin, GPIO.OUT)
        GPIO.setup(self.backwardPin, GPIO.OUT)   

    def __del__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup([self.forwardPin,self.backwardPin])


    def turnMotor(self, speed):
        if speed>0:
            # Set up PWM on forwards pin
            self.pwmF = GPIO.PWM(self.forwardPin, 1000)     # 1000 dutycycle
            self.pwmF.start(0)                              # start at 0 dutycycle
            self.pwmF.ChangeDutyCycle(abs(speed))           # change duty cycle to match speed
            GPIO.output(self.forwardPin, True)

            # Set backwards pin off
            self.pwmB = None
            GPIO.output(self.backwardPin, False)

        else:
            # Set up PWM on backwards pin
            self.pwmB = GPIO.PWM(self.backwardPin, 1000)     # 1000 dutycycle
            self.pwmB.start(0)                               # start at 0 dutycycle
            self.pwmB.ChangeDutyCycle(abs(speed))            # change duty cycle to match speed
            GPIO.output(self.backwardPin, True)

            # Set forwards pin off
            self.pwmF = None
            GPIO.output(self.forwardPin, False)


    def stopMotor(self):   
        GPIO.output(self.forwardPin, False)
        GPIO.output(self.backwardPin, False)
        if self.pwmF is not None:
             self.pwmF.stop()   
             self.pwmF = None
        if self.pwmB is not None:    
            self.pwmB.stop()     
            self.pwmB = None

# ======================================================================================================
# Main program
# =====================================================================================================

motor1 = RawMotorL9110S(forwardPin=24, backwardPin=23)
motor1.turnMotor(100)
sleep(2)    
motor1.turnMotor(-100)
sleep(2)
motor1.turnMotor(20)
sleep(2)    
motor1.turnMotor(-30)
sleep(2)
motor1.stopMotor()
print("Stopped motor 1")

motor2 = RawMotorL9110S(forwardPin=20, backwardPin=21)
motor2.turnMotor(100)
sleep(2)    
motor2.turnMotor(-100)
sleep(2)
motor2.turnMotor(20)
sleep(2)    
motor2.turnMotor(-30)
sleep(2)
motor2.stopMotor()
print("Stopped motor 2")
