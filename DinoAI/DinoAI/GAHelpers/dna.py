#  Copyright (c) 2020.
#  By Jorn Schampheleer

import random


class DNA(object):
    def __init__(self, lower_jump_trigger=20, upper_jump_trigger=200, lower_crouch_trigger=20, upper_crouch_trigger=200,
                 lower_object_height_trigger=20, upper_object_height_trigger=200):
        self.jump_trigger = random.randint(lower_jump_trigger, upper_jump_trigger)
        self.crouch_trigger = random.randint(lower_crouch_trigger, upper_crouch_trigger)
        self.object_height_trigger = random.randint(lower_object_height_trigger, upper_object_height_trigger)

    def copy(self):
        dna = DNA()
        dna.crouch_trigger = self.crouch_trigger
        dna.jump_trigger = self.jump_trigger
        dna.object_height_trigger = self.object_height_trigger
        return dna

    def __str__(self):
        return "[%d, %d, %d]" % (self.jump_trigger, self.crouch_trigger, self.object_height_trigger)
