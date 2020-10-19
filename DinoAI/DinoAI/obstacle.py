#  Copyright (c) 2020.
#  By Jorn Schampheleer
#  Textures copyrighted by google, extracted from the game by chirag64 (https://github.com/chirag64/t-rex-runner-bot)
import pygame
import random

OBSTACLE_TEXTURES_SMALL = [
    pygame.image.load("img/cactus1S.png"),
    pygame.image.load("img/cactus2S.png"),
    pygame.image.load("img/cactus3S.png")
]

OBSTACLE_TEXTURES_LARGE = [
    pygame.image.load("img/cactus1L.png"),
    pygame.image.load("img/cactus2L.png"),
    pygame.image.load("img/cactus3L.png")
]

ALL_TEXTURES = OBSTACLE_TEXTURES_LARGE + OBSTACLE_TEXTURES_SMALL

VELOCITY = 300

# Make sure the cacti are a little bit inside of the ground
Y_OFFSET = 12


class Obstacle(object):
    def __init__(self, surfacewidth, surfaceheight, texture=None):
        self.x = surfacewidth
        self.y = surfaceheight
        self.texture = random.choice(ALL_TEXTURES) if texture is None else ALL_TEXTURES[texture]
        self.y = surfaceheight - self.texture.get_size()[1] + Y_OFFSET
        self.mask = pygame.mask.from_surface(self.texture)

    def update(self, deltatime):
        self.x -= VELOCITY * deltatime

    def draw(self, display):
        display.blit(self.texture, (self.x, self.y))

    def is_offscreen(self):
        return self.x < 0

    def is_colliding(self, dinosaur):
        return self.mask.overlap(dinosaur.mask, (int(dinosaur.x - self.x), int(dinosaur.get_absolute_y() - self.y)))
