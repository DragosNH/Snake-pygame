import pygame
import time
import random

snake_speed = 15

# Widow size
window_x = 720
window_y = 480

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


pygame.init()

pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [100, 50]

# Initial snake body
snake_body = [
        [100, 50],
        [90, 50],
        [80,50],
        [70,50]
    ]

# Fruit position
fruit_position = [random.randrange(1, (window_x//10) * 10),
                  random.randrange(1, (window_y//10) * 10)]
fruit_spawn = True

# Default snake direction
direction = 'RIGHT'
change_to = direction

# --- Score area ---
score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)

    score_surface = score_font.render('Score : ' + str(score), True, color)

    score_rect = score_surface.get_rect()

    game_window.blit(score_surface, score_rect)
