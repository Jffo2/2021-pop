#  Copyright (c) 2020.
#  By Jorn Schampheleer
#  Textures copyrighted by google, extracted from the game by chirag64 (https://github.com/chirag64/t-rex-runner-bot)
import pygame
from DinoAI.DinoAI.dinosaur import Dinosaur
from DinoAI.DinoAI.aidinobehavior import AIDinoBehavior
from DinoAI.DinoAI.dna import DNA
import random

# region Textures
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

class AIDinosaur(Dinosaur):
    def __init__(self, surfaceheight):
        super().__init__(surfaceheight)
        self.dna = DNA()
        self.alive = True
        self.score = 0
        self.behavior = AIDinoBehavior(self.dna)

    def react(self, gamestate):
        jump, crouch = self.behavior.react(*gamestate)
        if jump:
            self.jump()
        self.set_crouch(crouch)

    def reset(self):
        self.alive = True
        self.score = 0
        self.y = 0
        self.yvelocity = 0
        self.crouching = False

    def increase_speed(self, newspeed):
        self.speed = newspeed

    @staticmethod
    def from_dinosaur(dinosaur):
        newdino = AIDinosaur(dinosaur.surfaceheight)
        newdino.dna = dinosaur.dna.copy()
        newdino.score = 0
        newdino.behavior = AIDinoBehavior(newdino.dna)
        return newdino
