import pygame
from pygame.locals import *
from constantes.py import *
from classes.py import *

pygame.init()
fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("Img/fond.png")
balle = pygame.image.load("Img/balle.png").convert_alpha()
fond = pygame.image.load("Img/raquette.png").convert_alpha()

continuer = 1
menu = 1
jeu = 1

while continuer = 1:
    print("Appuyez sur n'importe quelle touche pour démarer")
    while menu = 1:
        for event in pygame.event.get()
            if event.type == KEYDOWN:
                menu = 0
                jeu = 1
    while jeu == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                menu = 1
                jeu = 0
