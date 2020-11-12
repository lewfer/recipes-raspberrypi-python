from elsi_temperaturesensor import *
from time import sleep

t = TemperatureSensor(0)
while True:
    temp = t.read()
    print(temp)
    sleep(1)

