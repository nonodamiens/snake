import pygame
from pygame.locals import *

# Initialisation de pygame
pygame.init()

# Title
pygame.display.set_caption("SNAKE")

# création d'une fenetre avec fond vert
fenetre = pygame.display.set_mode((100, 100))
fenetre.fill([0,250,0])

# Création du sprite snake
snake_head = pygame.draw.rect(fenetre, [0, 0, 250], (0,0,10,10))
print(snake_head.x)
# snake head position
# snake_position = snake_head.get_rect()

# ajout d'un background ou d'une couleur de fond
# fond = pygame.image.load("background.png").convert()


# affichage du fond dans la fenetre
# fenetre.blit(fond, (0, 0))

# Ajout d'un personnage et enregistrement position
# perso = pygame.image.load("perso.png").convert_alpha()
# position_perso = perso.get_rect(center=(300, 200))
# fenetre.blit(perso, position_perso)
# print(type(perso))
# rafraichissement de la fenetre pour afficher l'image de fond
pygame.display.flip()

# Répétition si touche enfoncé
pygame.key.set_repeat(400, 30)

# print des infos
print(pygame.display.Info())
print(pygame.get_sdl_version())

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_RIGHT and snake_head.x < 90:
                snake_head.move_ip(10, 0)
            if event.key == K_LEFT  and snake_head.x > 0:
                snake_head.move_ip(-10, 0)
            if event.key == K_DOWN  and snake_head.y < 90:
                snake_head.move_ip(0, 10)
            if event.key == K_UP  and snake_head.y > 0:
                snake_head.move_ip(0, -10)
    fenetre.fill([0,250,0])            
    pygame.draw.rect(fenetre, (0, 0, 250), snake_head)
    # fenetre.blit(fond, (0, 0))
    # fenetre.blit(snake_head, (snake_head.x, snake_head.y))
    pygame.display.flip()