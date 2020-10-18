import pygame

dinocolour = 255, 255, 255
DINOHEIGHT = 40
DINOWIDTH = 20
WALK_SPRITE_ARRAY = [
    pygame.image.load("img/trex_walk3.png"),
    pygame.image.load("img/trex_walk4.png"),
]
JUMP_SPRITE = pygame.image.load("img/trex_walk1.png")
DEAD_SPRITE = pygame.image.load("img/trex_walk5.png")

UPDATE_SPRITE_EVERY = 3

GRAVITY = -1300
JUMP_VELOCITY = 500


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

    def jump(self):  # When adding classes into function, the first parameter must be the parameter
        if self.y == 0:  # Only allow jumping if the dinosaur is on the ground to prevent mid air jumps.
            self.yvelocity = JUMP_VELOCITY

    def update(self, deltatime):  # Updates the y position of the dinosaur each second
        self.yvelocity += GRAVITY * deltatime  # Gravity
        self.y += self.yvelocity * deltatime
        if self.y < 0:  # if the dinosaur sinks into the ground, make velocity and y = 0
            self.y = 0
            self.yvelocity = 0
        self.tick += 1
        if self.tick % UPDATE_SPRITE_EVERY == 0:
            self.sprite_index = (self.sprite_index + 1) % len(WALK_SPRITE_ARRAY)

    def draw(self, display):
        # pygame.draw.rect(display, dinocolour,
        #                 [self.x, self.surfaceHeight - self.y - self.height, self.width, self.height])
        if self.y == 0:
            display.blit(WALK_SPRITE_ARRAY[self.sprite_index], (self.x, self.surfaceHeight - self.y - self.height))
        else:
            display.blit(JUMP_SPRITE, (self.x, self.surfaceHeight - self.y - self.height))
