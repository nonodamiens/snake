import pygame
from pygame.locals import *

# Initialisation de pygame
pygame.init()

# création d'une fenetre avec fond vert
fenetre = pygame.display.set_mode((100, 100))
fenetre.fill([0,250,0])

# ajout d'un background ou d'une couleur de fond
# fond = pygame.image.load("background.png").convert()


# affichage du fond dans la fenetre
# fenetre.blit(fond, (0, 0))

# Ajout d'un personnage et enregistrement position
perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect(center=(300, 200))
fenetre.blit(perso, position_perso)

# rafraichissement de la fenetre pour afficher l'image de fond
pygame.display.flip()

# Répétition si touche enfoncé
pygame.key.set_repeat(400, 30)

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                position_perso = position_perso.move(3, 0)
            if event.key == K_LEFT:
                position_perso = position_perso.move(-3, 0)
            if event.key == K_DOWN:
                position_perso = position_perso.move(0, 3)
            if event.key == K_UP:
                position_perso = position_perso.move(0, -3)
    # fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, position_perso)
    pygame.display.flip()