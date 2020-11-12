import RPi.GPIO as GPIO
from time import sleep

# ======================================================================================================
# Stepper28BYJ48 class
# ======================================================================================================

class Stepper28BYJ48():
    
    def __init__(self, pin1, pin2, pin3, pin4, fullTurnSteps=512, delay=1):
        '''Initialise the stepper class'''

        GPIO.setmode(GPIO.BCM)                              # use BCM numbering
        GPIO.setwarnings(False)
        self.pin1 = pin1                                    # blue
        self.pin2 = pin2                                    # yellow
        self.pin3 = pin3                                    # pink
        self.pin4 = pin4                                    # orange
        self.fullTurnSteps = fullTurnSteps                  # number of steps to make 360 degrees
        self.delay = int(delay) / 1000.0                    # delay in milliseconds to add between steps
        self.stepError = 0                                  # cumulative error caused by rounding of number of steps

        #GPIO.setup(enable_pin, GPIO.OUT)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pin3, GPIO.OUT)
        GPIO.setup(self.pin4, GPIO.OUT)
 
        #GPIO.output(enable_pin, 1)

    def __del__(self):
        '''Reset the GPIO pins'''

        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup([self.pin1,self.pin2,self.pin3,self.pin4])
        
 
    def setStep(self, w1, w2, w3, w4):
        '''Output the given sequence of signals on the GPIO pins'''

        GPIO.output(self.pin1, w1)
        GPIO.output(self.pin2, w2)
        GPIO.output(self.pin3, w3)
        GPIO.output(self.pin4, w4)
 
    def forwardSteps(self, steps):
        '''To move the motor forwards we need to output signals on the 4 wires in the right forwards sequence'''

        for i in range(0, steps):
            self.setStep(0,0,0,1)
            sleep(self.delay)
            self.setStep(0,0,1,1)
            sleep(self.delay)
            self.setStep(0,0,1,0)
            sleep(self.delay)
            self.setStep(0,1,1,0)
            sleep(self.delay)
            self.setStep(0,1,0,0)
            sleep(self.delay)
            self.setStep(1,1,0,0)
            sleep(self.delay)
            self.setStep(1,0,0,0)
            sleep(self.delay)
            self.setStep(1,0,0,1)
            sleep(self.delay)

    def backwardSteps(self, steps):
        '''To move the motor forwards we need to output signals on the 4 wires in the right backwards sequence'''
        
        for i in range(0, steps):
            self.setStep(1,0,0,1)
            sleep(self.delay)
            self.setStep(1,0,0,0)
            sleep(self.delay)
            self.setStep(1,1,0,0)
            sleep(self.delay)
            self.setStep(0,1,0,0)
            sleep(self.delay)
            self.setStep(0,1,1,0)
            sleep(self.delay)
            self.setStep(0,0,1,0)
            sleep(self.delay)
            self.setStep(0,0,1,1)
            sleep(self.delay)
            self.setStep(0,0,0,1)
            sleep(self.delay)
 
    def forwardDegrees(self, degrees):
        '''Move stepper forwards by the given number of degrees.'''

        steps = degrees * self.fullTurnSteps / 360
        print("FWD Step error {:3.3f} Steps {:3.3f} int steps {:3.3f}".format(self.stepError, steps, int(steps)), end="")

        # If the above calculation gives a non-integer value we have a small error.  
        # Add these errors as we find them and move the motor an additional step if the error gets large enough
        error = steps-int(steps)                # calculate the error in this movement
        self.stepError += error                 # add this error to the total error
        if self.stepError >= 1:                 # if the error is bigger than one step
            print(" add +step ", end="")
            steps += 1                          # move forwards one more step
            self.stepError -= 1                 # reduce the error by one step

        self.forwardSteps(int(steps))

        print(" Step Error {:3.3f}".format(self.stepError))

    def backwardDegrees(self, degrees):
        '''Move stepper backwards by the given number of degrees.'''

        steps = degrees * self.fullTurnSteps / 360
        print("BWD Step error {:3.3f} Steps {:3.3f} int steps {:3.3f}".format(self.stepError, steps, int(steps)), end="")

        # If the above calculation gives a non-integer value we have a small error.  
        # Add these errors as we find them and move the motor an additional step if the error gets large enough
        error = steps-int(steps)                # calculate the error in this movement
        self.stepError -= error                 # add this error to the total error
        if self.stepError <= -1:                # if the error is bigger than one step
            print(" add -step ", end="")
            steps += 1                          # move forwards one more step
            self.stepError += 1                 # reduce the error by one step

        self.backwardSteps(int(steps))      

        print(" Step Error {:3.3f}".format(self.stepError))

    def moveByAngle(self, angle):
        '''Move the stepper by the given angle, forwards is positive, backwards is negative'''

        if angle<0:
            self.backwardDegrees(abs(angle))
        else:
            self.forwardDegrees(angle)

    def stop(self):
        '''Stop the stepper'''
        
        self.setStep(0,0,0,0)

        
