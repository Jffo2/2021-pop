#  Copyright (c) 2020.
#  By Jorn Schampheleer
#  Textures copyrighted by google, extracted from the game by chirag64 (https://github.com/chirag64/t-rex-runner-bot)
from DinoAI.DinoAI.GameObjects.dinosaur import Dinosaur
from DinoAI.DinoAI.GAHelpers.aidinobehavior import AIDinoBehavior
from DinoAI.DinoAI.GAHelpers.dna import DNA


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

    @staticmethod
    def from_dinosaur(dinosaur):
        """
        Copy a dinosaur. This returns a new alive dinosaur with score 0. It only copies DNA and behavior
        @param dinosaur: The dinosaur to copy
        @return: A new copied dinosaur
        """
        newdino = AIDinosaur(dinosaur.surfaceheight)
        newdino.dna = dinosaur.dna.copy()
        newdino.score = 0
        newdino.behavior = AIDinoBehavior(newdino.dna)
        return newdino
