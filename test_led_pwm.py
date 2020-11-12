from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

for brightness in range(0,100,10):
    led.value = brightness  / 100.0 
    sleep(1)
