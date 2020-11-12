from elsi_solenoid import *

m = SolenoidL9110S(triggerPin=24, groundPin=23)
m.fire()

m2 = SolenoidL9110S(triggerPin=23, groundPin=24)
m2.fire()

