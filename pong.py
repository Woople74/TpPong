import pygame
from pygame.locals import *
from classe import *
from constantes import *

pygame.init()
fenetre = pygame.display.set_mode((hauteurE, largeurE))
fond = pygame.image.load("Img/fond.png")

continuer = 1
menu = 1
jeu = 1

while continuer == 1:
    print("Appuyez sur n'importe quelle touche pour démarer")
    while menu == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                menu = 0
                jeu = 1
    while jeu == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                menu = 1
                jeu = 0
