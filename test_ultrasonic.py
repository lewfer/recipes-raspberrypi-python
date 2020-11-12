from elsi_ultrasonic import *

u = Ultrasonic(echo=20, trigger=21)
while True:
    dist = u.medianDistance()
    print ("Measured Distance = %.1f cm" % dist)
    sleep(1)
    
'''
# Using the gpiozero library

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=20, trigger=21, threshold_distance=0.1)
while True:
    print('Distance: ', sensor.distance * 100)
    sleep(1)
'''