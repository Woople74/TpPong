""" Fichiers regroupant toutes les classes de notre jeu :
    - Raquette
    - Balle """
from constantes.py import *
import pygame

class Raquette:
    def __init__(x):
        self.x = x
        self.y = 295
        self.direction = RIEN
        self.rect = Rect((self.x, self.y), (largeurP, hauteurP))
    def refresh(fenetre, img):
        self.y = VITESSE_RAQUETTE * self.direction  
        if self.y > hauteurP and self.y = 480 - hauteurP: 
            fenetre.blit(img, (self.x, self.y))
