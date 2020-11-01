#  Copyright (c) 2020.
#  By Jorn Schampheleer

class AIDinoBehavior(object):
    def __init__(self, dna):
        self.dna = dna

    def react(self, next_object_x, next_object_y):
        if next_object_y <= self.dna.object_height_trigger:
            should_jump = self._should_jump(next_object_x)
            should_crouch = False
        else:
            should_crouch = self._should_crouch(next_object_x)
            should_jump = False
        return should_jump, should_crouch

    def _should_jump(self, next_object_x):
        return self.dna.jump_trigger >= next_object_x

    def _should_crouch(self, next_object_x):
        return self.dna.crouch_trigger >= next_object_x
