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

# print des infos
print(pygame.display.Info())
print(pygame.get_sdl_version())

# Boucle
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

    fenetre.fill([0,250,0]) # 'clear' the surface
    pygame.draw.rect(fenetre, (0, 0, 250), snake_head) # draw the new rectangle
    pygame.display.flip()