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
snake_direction = "D" # initialize snake direction to down
snake_speed = 500
snake_move = USEREVENT + 1
pygame.time.set_timer(snake_move, snake_speed)

# print des infos
print(pygame.display.Info())
print(pygame.get_sdl_version())

# Boucle
continuer = 1
while continuer:
    for event in pygame.event.get() :
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                snake_direction = "R"
            if event.key == K_LEFT:
                snake_direction = "L"
            if event.key == K_DOWN:
                snake_direction = "D"
            if event.key == K_UP:
                snake_direction = "U"
        if event.type == snake_move:
            if snake_direction == "R"  and snake_head.x < 90:
                snake_head.move_ip(10, 0)
            if snake_direction == "L"  and snake_head.x > 0:
                snake_head.move_ip(-10, 0)
            if snake_direction == "D"  and snake_head.y < 90:
                snake_head.move_ip(0, 10)
            if snake_direction == "U"  and snake_head.y > 0:
                snake_head.move_ip(0, -10)
        
    fenetre.fill([0,250,0]) # 'clear' the surface
    pygame.draw.rect(fenetre, (0, 0, 250), snake_head) # draw the new rectangle
    pygame.display.flip()