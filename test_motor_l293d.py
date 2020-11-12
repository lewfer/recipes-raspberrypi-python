from elsi_motorl293d import *
from time import sleep

m = MotorL293D(enablePin=26, forwardPin=20, backwardPin=21)
m.turnMotor(100)
sleep(2)    
m.turnMotor(-100)
sleep(2)
m.turnMotor(50)
sleep(2)    
m.turnMotor(-50)
sleep(2)
m.stopMotor()


