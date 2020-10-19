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

OBSTACLE_TEXTURES_BIRD = [
    pygame.image.load("img/bird_flap1.png"),
    pygame.image.load("img/bird_flap2.png")
]

ALL_TEXTURES = OBSTACLE_TEXTURES_LARGE + OBSTACLE_TEXTURES_SMALL + OBSTACLE_TEXTURES_BIRD

VELOCITY = 300

BIRD_FLAP_EVERY = 4

# Make sure the cacti are a little bit inside of the ground
Y_OFFSET = 12

BIRD_HEIGHT_ARRAY = [
    0,
    40,
    60
]


class Obstacle(object):
    def __init__(self, surfacewidth, surfaceheight, texture=None):
        self.bird = False
        self.x = surfacewidth
        self.y = surfaceheight
        self.texture = random.choice(ALL_TEXTURES) if texture is None else ALL_TEXTURES[texture]
        self.y = surfaceheight - self.texture.get_size()[1] + Y_OFFSET
        self.mask = pygame.mask.from_surface(self.texture)
        # Choose height for bird
        if self.texture in OBSTACLE_TEXTURES_BIRD:
            self.y -= random.choice(BIRD_HEIGHT_ARRAY)
            self.bird = True
            self.sprite_index = 0
            self.mask = [
                pygame.mask.from_surface(OBSTACLE_TEXTURES_BIRD[0]),
                pygame.mask.from_surface(OBSTACLE_TEXTURES_BIRD[1])
            ]
        self.tick = 0

    def update(self, deltatime):
        self.x -= VELOCITY * deltatime
        self.tick += 1
        if self.bird and self.tick % BIRD_FLAP_EVERY == 0:
            self.sprite_index = (self.sprite_index + 1) % len(OBSTACLE_TEXTURES_BIRD)

    def draw(self, display):
        texture = OBSTACLE_TEXTURES_BIRD[self.sprite_index] if self.bird else self.texture
        display.blit(texture, (self.x, self.y))

    def is_offscreen(self):
        return self.x < 0

    def is_colliding(self, dinosaur):
        if self.bird:
            mask = self.mask[self.sprite_index]
        else:
            mask = self.mask
        return mask.overlap(dinosaur.get_mask(),
                            (int(dinosaur.x - self.x), int(dinosaur.get_absolute_y() - self.y)))
