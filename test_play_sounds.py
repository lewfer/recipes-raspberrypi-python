import pygame

# Play a track
pygame.mixer.init()
pygame.mixer.music.load("/usr/share/sounds/alsa/Front_Center.wav")
pygame.mixer.music.play()

# Wait for the track to complete
while pygame.mixer.music.get_busy():
    continue