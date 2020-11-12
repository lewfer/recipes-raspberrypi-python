from picamera import PiCamera
from time import sleep

# Prepare the camera module
camera = PiCamera()
camera.rotation = 270

# Preview image for 5 seconds
camera.start_preview()
print("Taking picture in 5 seconds...")
sleep(1)
print("...4...")
sleep(1)
print("...3...")
sleep(1)
print("...4...")
sleep(1)
print("...1...")
sleep(1)
camera.stop_preview()

# Take a picture
camera.capture("tclimage.jpg")