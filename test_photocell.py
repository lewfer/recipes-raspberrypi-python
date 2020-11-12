from gpiozero import LightSensor
from time import sleep

p = LightSensor(26)

while True:
    print (p.value)
    sleep(0.1)
