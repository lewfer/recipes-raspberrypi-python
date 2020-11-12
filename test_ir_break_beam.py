from gpiozero import Button
from time import sleep

ir = Button(18)

while True:
    if ir.is_pressed:
        print("Broken")
    else:
        print("Not broken")
    sleep(0.2)