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
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'{current_dir}{img_folder}bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.val = 0
        self.clicked = False

    def update_bird(self):
        if flying:
            # gravatiy check
            self.val += .5  # the graviaty gone increase until reach to 8
            if self.val > 8:
                self.val = 8
            if self.rect.bottom < 786:
                self.rect.y += int(self.val)

        # checking game Over
        if game_over == False:
            # jump
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.clicked == False:
                        self.clicked = True
                        self.y = -10
                    if self.clicked:
                        self.clicked = False
            # hanlde animation
            self.counter += 1
            flap_cooldown = 10
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1

                # now check if the last image or not
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.images[self.index], self.val * -2)
            
        # handle the bird dead
        else: 
            self.image = pygame.transform.rotate(self.images[self.index] , -90)

# create instance from the class bird
bird_group = pygame.sprite.Group()
flappy = Bird(100, int(SCREEN_HEIGHT / 2))
bird_group.add(flappy)

run = True
while run:
    clock.tick(fbs)

    # display the images for the background
    screen.blit(bg, (0, 0))

    # draw the bird
    bird_group.draw(screen)
    bird_group.update()
    flappy.update_bird()

    screen.blit(ground_image, (ground_scroll, 768))

    # start scroll the ground if the flappy bird not dead
    if game_over == False:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0


    # login for game_over
    if flappy.rect.bottom > 768:
        game_over = True
        flying = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()
pygame.quit()
