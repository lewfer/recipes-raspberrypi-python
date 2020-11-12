from elsi_membranekeypad import *

keypad = MembraneKeypad(rowPins = [6,13,19,26], colPins = [12,16,20,21])

while True:
        print(keypad.getPress())