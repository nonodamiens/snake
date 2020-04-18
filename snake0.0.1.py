import pygame
# importatio de constantes de pygame
from pygame.locals import *

# Initialisation de pygame
pygame.init()

# création d'une fenetre
fenetre = pygame.display.set_mode((640, 480))

# ajout d'un background
fond = pygame.image.load("background.png").convert()

# affichage du fond dans la fenetre
fenetre.blit(fond, (0, 0))

# Ajout d'un personnage
perso = pygame.image.load("perso.png").convert_alpha()
fenetre.blit(perso, (200, 300))

# rafraichissement de la fenetre pour afficher l'image de fond
pygame.display.flip()