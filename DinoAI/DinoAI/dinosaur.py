#  Copyright (c) 2020.
#  By Jorn Schampheleer
#  Textures copyrighted by google, extracted from the game by chirag64 (https://github.com/chirag64/t-rex-runner-bot)
import pygame

DINOHEIGHT = 40
DINOWIDTH = 20
WALK_SPRITE_ARRAY = [
    pygame.image.load("img/trex_walk3.png"),
    pygame.image.load("img/trex_walk4.png"),
]
JUMP_SPRITE = pygame.image.load("img/trex_walk1.png")
DEAD_SPRITE = pygame.image.load("img/trex_walk5.png")

UPDATE_SPRITE_EVERY = 3

GRAVITY = -2500
JUMP_VELOCITY = 800


class Dinosaur(object):
    def __init__(self, surfaceheight):
        self.x = 60
        self.y = 0
        self.yvelocity = 0
        self.height = DINOHEIGHT
        self.width = DINOWIDTH
        self.surfaceHeight = surfaceheight
        self.tick = 0
        self.sprite_index = 0
        # Jump sprite is the most neutral one for collision detection, with the legs in the center
        # The other image move their legs a tiny bit but this is not significant
        self.mask = pygame.mask.from_surface(JUMP_SPRITE)

    def jump(self):
        if self.y == 0:
            self.yvelocity = JUMP_VELOCITY

    def update(self, deltatime):
        self.yvelocity += GRAVITY * deltatime
        self.y += self.yvelocity * deltatime
        if self.y < 0:
            self.y = 0
            self.yvelocity = 0
        self.tick += 1
        if self.tick % UPDATE_SPRITE_EVERY == 0:
            self.sprite_index = (self.sprite_index + 1) % len(WALK_SPRITE_ARRAY)

    def draw(self, display):
        if self.y == 0:
            display.blit(WALK_SPRITE_ARRAY[self.sprite_index], (self.x, self.surfaceHeight - self.y - self.height))
        else:
            display.blit(JUMP_SPRITE, (self.x, self.surfaceHeight - self.y - self.height))

    def get_absolute_y(self):
        return self.surfaceHeight - self.y - self.height
