#  Copyright (c) 2020.
#  By Jorn Schampheleer
#  Textures copyrighted by google, extracted from the game by chirag64 (https://github.com/chirag64/t-rex-runner-bot)
import pygame

# region textures
WALK_SPRITE_ARRAY = [
    pygame.image.load("img/trex_walk3.png"),
    pygame.image.load("img/trex_walk4.png"),
]
CROUCH_SPRITE_ARRAY = [
    pygame.image.load("img/trex_duck1.png"),
    pygame.image.load("img/trex_duck2.png"),
]

JUMP_SPRITE = pygame.image.load("img/trex_walk1.png")
DEAD_SPRITE = pygame.image.load("img/trex_walk5.png")
# endregion

# region Static vars
UPDATE_SPRITE_EVERY = 3

GRAVITY = -2500
JUMP_VELOCITY = 800

WALK_HEIGHT = JUMP_SPRITE.get_size()[1]
WALK_WIDTH = JUMP_SPRITE.get_size()[0]

CROUCH_HEIGHT = CROUCH_SPRITE_ARRAY[0].get_size()[1]
CROUCH_WIDTH = CROUCH_SPRITE_ARRAY[0].get_size()[0]

Y_OFFSET = 15


# endregion

class Dinosaur(object):
    def __init__(self, surfaceheight):
        self.crouching = False
        self.x = 60
        self.y = 0
        self.yvelocity = 0
        self.surfaceheight = surfaceheight
        self.tick = 0
        self.sprite_index = 0
        # Jump sprite is the most neutral one for collision detection, with the legs in the center
        # The other image move their legs a tiny bit but this is not significant
        self.walk_mask = pygame.mask.from_surface(JUMP_SPRITE)
        self.crouch_mask = pygame.mask.from_surface(CROUCH_SPRITE_ARRAY[0])

    @property
    def height(self):
        return CROUCH_HEIGHT if self.crouching else WALK_HEIGHT

    @property
    def width(self):
        return CROUCH_WIDTH if self.crouching else WALK_WIDTH

    def jump(self):
        if self.y == 0:
            self.yvelocity = JUMP_VELOCITY
            self.crouching = False

    def set_crouch(self, crouching):
        if self.y == 0:
            self.crouching = crouching

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
            if self.crouching:
                array_to_use = CROUCH_SPRITE_ARRAY
            else:
                array_to_use = WALK_SPRITE_ARRAY
            display.blit(array_to_use[self.sprite_index], (self.x, self.get_absolute_y()))
        else:
            display.blit(JUMP_SPRITE, (self.x, self.get_absolute_y()))

    def get_absolute_y(self):
        return self.surfaceheight - self.y - self.height + Y_OFFSET

    def get_mask(self):
        return self.crouch_mask if self.crouching else self.walk_mask
