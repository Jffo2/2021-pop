#  Copyright (c) 2020.
#  By Jorn Schampheleer
#  Textures copyrighted by google, extracted from the game by chirag64 (https://github.com/chirag64/t-rex-runner-bot)
from DinoAI.DinoAI.GameObjects.dinosaur import Dinosaur
import neat


class NeatDinosaur(Dinosaur):
    def __init__(self, surfaceheight, genome, config):
        super().__init__(surfaceheight)
        self.alive = True
        self.genome = genome
        self.config = config
        self.neural_network = neat.nn.FeedForwardNetwork.create(genome, config)
        self.score = 0

    def react(self, gamestate):
        # Use the neural network to react
        output = self.neural_network.activate(gamestate)
        crouch = output[1] > 0.5
        jump = output[0] > 0.5 and not crouch
        if jump:
            self.jump()
        self.set_crouch(crouch)
