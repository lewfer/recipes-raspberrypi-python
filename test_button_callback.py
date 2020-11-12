from gpiozero import Button

def callback(button):
    print("Pressed button on", button.pin)

b1 = Button(26) 
b2 = Button(21) 

print("Waiting for callback")
b1.when_pressed = callback
b2.when_pressed = callback

# Loop until Ctrl-C pressed 
while True:
    pass