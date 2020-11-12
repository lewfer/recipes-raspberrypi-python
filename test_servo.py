from gpiozero import Servo
from time import sleep

servo = Servo(21, frame_width=0.02, min_pulse_width = 0.0006, max_pulse_width = 0.0023)

while True:
    servo.value = -1
    sleep(1)
    servo.value = 0
    sleep(1)
    servo.value = 1
    sleep(1)
