from elsi_motor_cytron_md10c import *
from time import sleep

motor = MotorMD10C(20, 21)

# Forwards
for speed in range(0,110,10):
    print(speed)
    motor.turnMotor(speed)
    sleep(1)

# Backwards
for speed in range(0,110,10):
    print(-speed)
    motor.turnMotor(-speed)
    sleep(1)

#motor.turnMotor(0)
