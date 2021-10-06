# Faça um programa em Python3 que abra e reproduza um arquivo de música MP3:

import pygame
pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()
