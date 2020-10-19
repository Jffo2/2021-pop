#  Copyright (c) 2020.
#  By Jorn Schampheleer
#  Textures copyrighted by google, extracted from the game by chirag64 (https://github.com/chirag64/t-rex-runner-bot)
import pygame

GROUND_SPRITE = pygame.image.load("img/ground.png")
WIDTH = GROUND_SPRITE.get_size()[0]
VELOCITY = 300


class Ground(object):
    def __init__(self, surfaceheight, ground_height):
        self.x = 0
        self.y = surfaceheight - ground_height

    def update(self, deltatime):
        self.x -= VELOCITY * deltatime
        if self.x <= -1 * GROUND_SPRITE.get_size()[0]:
            self.x = 0

    def draw(self, display):
        display.blit(GROUND_SPRITE, (self.x, self.y))
        display.blit(GROUND_SPRITE, (self.x+WIDTH, self.y))
