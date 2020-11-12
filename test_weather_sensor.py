# Think Create Learn
#
# ELSI Test Weather Sensor
#
# 2018 Llewelyn Fernandes
#

from elsi_weathersensor import *
from time import sleep

ws = WeatherSensor()

while True:
    data = ws.read()
    print(data.humidity, data.pressure, data.temperature)
    sleep(1)
    
