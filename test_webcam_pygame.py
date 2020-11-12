import os
import pygame, sys

from pygame.locals import *
import pygame.camera

width = 640
height = 480

# Initialise pygame   
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(width,height))
cam.start()

# Setup window
windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
pygame.display.set_caption('Camera')

# Take a picture
image = cam.get_image()
cam.stop()

# Display the picture
catSurfaceObj = image
windowSurfaceObj.blit(catSurfaceObj,(0,0))
pygame.display.update()

# Save picture
pygame.image.save(windowSurfaceObj,'image.jpg')