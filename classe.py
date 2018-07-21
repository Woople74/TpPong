""" Fichiers regroupant toutes les classes de notre jeu :
    - Raquette
    - Balle """
import pygame
from constantes import *

class Raquette:
    def __init__(x):
        self.x = x
        self.y = 295
        self.direction = RIEN
        slef.image = pygame.image.load("Img/raquette.png").convert_alpha()
        self.rect = Rect((self.x, self.y), (largeurP, hauteurP))
    def moove(fenetre, img):
        self.y = VITESSE_RAQUETTE * self.direction  
        if self.y > hauteurP and self.y == 480 - hauteurP: 
            fenetre.blit(img, (self.x, self.y))
    def collide(balle)
        if self.rect.collide(balle) == True:
            return True

class Balle:
    def __init__():
        self.image = pygame.image.load("Img/balle.png").convert_alpha()
        self.x = (largeurE/2) - 10
        self.y = (hauteurE/2) - 10
        self.vect = [VITESSE_BALLE, -VITESSE_BALLE]
        self.rect = Rect((self.x, self.y), (20,20))
    def refresh(listraquette):
        #Utiliser raquette.collide + la taille de l'écran pour déterminer si la balle doit rebondir
        #Si on tape par le haut on change la direction en y (négatif) en ajoutant du hasard et on ajoute juste du hasard sur le x
        #L'inverse si on tape sur les cotés (On peut faire raquette pour cotés et bors de l'écrans pour le haut car 
        #si la raquette loupe la balle on perd la partie
        if raquette.collide(self.rect) == True :
            self.vect[0] = -self.rect[0] + randint(100,180)
            self.vect[1] += randint(100,180) 
        if self.y < 0 or self.y > largeurE - 20:
            self.vect[0]
        self.x += self.vect[0]
        self.y += self.vect[1]
