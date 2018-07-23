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
                raquette1 = Raquette(20)
                raquette2 = Raquette(largeurE - 20)
                balle = Balle(fenetre)
                game = Game()
                menu = 0
                jeu = 1
                game.prepare(balle)
    while jeu == 1:
        """Appele toutes les méthodes de Game dans cet ordre :
            -Prepare
            boucle while :
                boucle for des évenements
                update
                déplacement de la balle
                pygame.display.flip"""
        fenetre.blit(fond, (0,0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu = 1
                    jeu = 0
                if event.key == K_z:
                    raquette1.moove(HAUT)
                if event.key == K_s:
                    raquette2.moove(BAS)
                if event.key == K_UP:
                    raquette2.moove(HAUT)
                if event.key == K_DOWN:
                    raquette2.moove(BAS)
        balle.refresh(raquette1, raquette2)
        pygame.display.flip()


