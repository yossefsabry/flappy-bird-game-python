import pygame
from pygame.locals import *

pygame.init()

# start frame for the game
clock = pygame.time.Clock()
fbs = 60

screen_width = 864
screen_height = 936

# define game variblaes
ground_scroll = 0
scroll_speed = 4

# load images
bg = pygame.image.load('include/img/bg.png')
ground_img = pygame.image.load('include/img/ground.png')

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Flappy Bird')
run = True
while run:

    clock.tick(fbs)

    # display bg and grouwnd image
    screen.blit(bg, (0,0))
    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()