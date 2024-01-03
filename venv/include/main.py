import pygame
from pygame.locals import *
import os

# initailzation for pygame :: like setup all the things in pygame
pygame.init()

# start frame for the game
clock = pygame.time.Clock()
fbs = 60

# setup for the window
SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("welcome in flappy bird game")

# define game variables
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False

# add changes in git

# load images for the game
current_dir = os.getcwd()
img_folder = "/venv/include/img/"
bg = pygame.image.load(f'{current_dir}{img_folder}bg.png')
ground_image = pygame.image.load(f'{current_dir}{img_folder}ground.png')


# start bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y


run = True
while run:
    clock.tick(fbs)

    # display the images for the background
    screen.blit(bg, (0, 0))
    screen.blit(ground_image, (ground_scroll, 768))

    # start scroll the ground
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()
pygame.quit()
