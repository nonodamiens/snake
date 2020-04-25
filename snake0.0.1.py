import pygame
from pygame.locals import *
import random

# Initialisation de pygame
pygame.init()

# Title
pygame.display.set_caption("SNAKE")

# création d'une fenetre avec fond vert
fenetre = pygame.display.set_mode((100, 100))
fenetre.fill([0,250,0])

# Création du sprite snake
snake_head = pygame.draw.rect(fenetre, [0, 0, 250], (40,40,10,10))
snake_direction = "D" # initialize snake direction to down
snake_speed = 500
snake_move = USEREVENT + 1
pygame.time.set_timer(snake_move, snake_speed)
snake_tail = pygame.draw.rect(fenetre, [0, 0, 200], (40, 30, 10, 10))
snake_tail_2 = snake_tail.copy()
snake_tail_2.move_ip(0, -10)
snake_tail_positions = [snake_tail, snake_tail_2]

# Création d'un sprite pomme
apple_x = random.randint(0, 9) * 10
apple_y = random.randint(0, 9) * 10
while apple_x == 40:
    apple_x = random.randint(0, 9) * 10
while apple_y == 40:
    apple_y = random.randint(0, 9) * 10
apple = pygame.draw.rect(fenetre, [250, 0, 0], (apple_x, apple_y, 10, 10))
apple_ate = False

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
                if apple_ate:
                    snake_tail_positions = [snake_head.copy()] + snake_tail_positions
                    apple_ate = False
                else:
                    snake_tail_positions = [snake_head.copy()] + snake_tail_positions[:-1]
                snake_head.move_ip(10, 0)
            if snake_direction == "L"  and snake_head.x > 0:
                if apple_ate:
                    snake_tail_positions = [snake_head.copy()] + snake_tail_positions
                    apple_ate = False
                else:
                    snake_tail_positions = [snake_head.copy()] + snake_tail_positions[:-1]
                snake_head.move_ip(-10, 0)
            if snake_direction == "D"  and snake_head.y < 90:
                if apple_ate:
                    snake_tail_positions = [snake_head.copy()] + snake_tail_positions
                    apple_ate = False
                else:
                    snake_tail_positions = [snake_head.copy()] + snake_tail_positions[:-1]
                snake_head.move_ip(0, 10)
            if snake_direction == "U"  and snake_head.y > 0:
                if apple_ate:
                    snake_tail_positions = [snake_head.copy()] + snake_tail_positions
                    apple_ate = False
                else:
                    snake_tail_positions = [snake_head.copy()] + snake_tail_positions[:-1]
                snake_head.move_ip(0, -10)
        if snake_head.x == apple.x and snake_head.y == apple.y:
            apple_ate = True
            while apple.x == snake_head.x:
                apple.x = random.randint(0, 9) * 10
            while apple.y == snake_head.y:
                apple.y = random.randint(0, 9) * 10
        
    fenetre.fill([0,250,0]) # 'clear' the surface
    pygame.draw.rect(fenetre, (250, 0, 0), apple) # draw the apple
    for tail in snake_tail_positions[:-1]:
        print(tail)
        pygame.draw.rect(fenetre, (0, 0, 200), tail)
    pygame.draw.rect(fenetre, (0, 0, 250), snake_head) # draw the new rectangle

    pygame.display.flip()