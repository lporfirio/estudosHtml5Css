# faça um programa que abra e reproduza um arquivo em mp3.

'''import pygame
pygame.init()
pygame.mixer.music.load('track10.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

import playsound
playsound.playsound("track10.mp3")