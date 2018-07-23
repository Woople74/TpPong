""" Fichiers regroupant toutes les classes de notre jeu :
    - Raquette
    - Balle """
import pygame
from pygame.locals import *
from constantes import *

class Raquette:
    def __init__(self, x):
        self.x = x
        self.y = 295
        self.direction = RIEN
        self.image = pygame.image.load("Img/raquette.png").convert_alpha()
        self.rect = Rect((self.x, self.y), (largeurP, hauteurP))
    def moove(self, fenetre):
        self.y = VITESSE_RAQUETTE * self.direction  
        if self.y > hauteurP and self.y == 480 - hauteurP: 
            fenetre.blit(self.image, (self.x, self.y))
    def collide(self, balle):
        if self.rect.collide(balle) == True:
            return True

class Balle:
    def __init__(self, ecran: pygame.surface):
        self.image = pygame.image.load("Img/balle.png").convert_alpha()
        self.x = (largeurE/2) - 10
        self.y = (hauteurE/2) - 10
        self.vect = [VITESSE_BALLE, -VITESSE_BALLE]
        self.rect = Rect((self.x, self.y), (20,20))
        self.ecran = ecran
    def refresh(self, raquette1, raquette2):
        if raquette1.collide(self.rect) == True :
            self.vect[0] = -self.rect[0] + (randint(100,180) / 1000)
            self.vect[1] += (randint(100,180) / 1000) 
        if raquette2.collide(self.rect) == True :
            self.vect[1] = -self.rect[1] + (randint(100,180) / 1000)
            self.vect[0] += (randint(100,180) / 1000) 
        if self.y < 0 or self.y > largeurE - 20:
            self.vect[0]
        self.x += self.vect[0]
        self.y += self.vect[1]

class Game:
    def prepare(self, balle):
        """Méthode qui se charge de tout remettre a 0 si besoin"""
        balle.vect = [VITESSE_BALLE, -VITESSE_BALLE]
        balle.x = (largeurE/2) - 10
        balle.y = (hauteurE/2) - 10
        score_1 = 0
        score_2 = 0
