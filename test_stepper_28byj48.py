from elsi_stepper28byj48 import *

steps = 512

stepper = Stepper28BYJ48(pin1=12, pin2=16, pin3=20, pin4=21, fullTurnSteps=512)
stepper.forwardSteps(steps)
sleep(1)            
stepper.backwardSteps(steps)
sleep(1)        
stepper.stop()    

