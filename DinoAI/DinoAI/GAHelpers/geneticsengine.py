#  Copyright (c) 2020.
#  By Jorn Schampheleer

from DinoAI.DinoAI.GameObjects.aidinosaur import AIDinosaur
from DinoAI.DinoAI.GAHelpers.dna import DNA
import random

POPULATION_SIZE = 20
N_GENERATIONS = 1000
MUTATION_CHANCE = 0.1


class GeneticsEngine(object):
    def __init__(self, surfaceheight, amount_dinosaurs=POPULATION_SIZE, n_generations=N_GENERATIONS,
                 mutation_chance=MUTATION_CHANCE):
        self.n_generations = N_GENERATIONS
        self.current_gen = 1
        self.n_population = POPULATION_SIZE
        self.dinosaurs = self.gen_dinosaurs(amount_dinosaurs, surfaceheight)
        self.mutation_chance = mutation_chance
        self.best_dinosaur = self.dinosaurs[0]

    @staticmethod
    def gen_dinosaurs(amount_dinosaurs, surfaceheight):
        """
        Create amount_dinosaurs amount of AIDinosaurs
        @param amount_dinosaurs: the amount of dinosaurs to generate at random
        @param surfaceheight: necessary parameter to init dinosaurs
        @return: an array of AIDinosaurs
        """
        return [AIDinosaur(surfaceheight) for _ in range(amount_dinosaurs)]

    def select(self, amount=0.3):
        """
        Perform natural selection among dinosaurs
        @param amount: the amount of parents to select, default is 30%
        @return: the selected dinosaurs based on the selection algorithm
        """
        # t This is the ranked way
        fitscores = [dino.score for dino in self.dinosaurs]
        rank_weights = list(range(len(fitscores)))[::-1]
        sorted_individuals = [individual for fitness, individual in
                              sorted(zip(fitscores, self.dinosaurs), key=lambda x: self.best_dinosaur.score - x[0])]
        return random.choices(sorted_individuals, rank_weights, k=int((amount * len(self.dinosaurs))))

    @staticmethod
    def crossover(parent1: AIDinosaur, parent2):
        """
        Calculate two babies from 2 parents by swapping 1 of the properties from the parents
        @param parent1: The first parent
        @param parent2: The second parent
        @return: A tuple containing two babies
        """
        index = random.randint(1, 3)
        dinobaby1 = AIDinosaur.from_dinosaur(parent1)
        dinobaby2 = AIDinosaur.from_dinosaur(parent2)
        if index == 1:
            dinobaby1.dna.jump_trigger = parent2.dna.jump_trigger
            dinobaby2.dna.jump_trigger = parent1.dna.jump_trigger
        elif index == 2:
            dinobaby1.dna.crouch_trigger = parent2.dna.crouch_trigger
            dinobaby2.dna.crouch_trigger = parent1.dna.crouch_trigger
        else:
            dinobaby1.dna.object_height_trigger = parent2.dna.object_height_trigger
            dinobaby2.dna.object_height_trigger = parent1.dna.object_height_trigger
        return dinobaby1, dinobaby2

    def mate(self, fittest_individuals, amount):
        """
        Let the fittest individuals of the population reproduce.
        @param fittest_individuals: The individuals to mate
        @param amount: The amount of babies to make
        @return: A list of all the babies
        """
        babies = list()
        for i in range(0, amount, 2):
            baby1, baby2 = self.crossover(random.choice(fittest_individuals), random.choice(fittest_individuals))
            babies.append(baby1)
            if len(babies) >= amount:
                break
            babies.append(baby2)
        return babies

    def mutate(self, dinosaurs):
        """
        Allow DNA to mutate to a random value
        @param dinosaurs: the dinosaurs to mutate
        """
        for dino in dinosaurs:
            if random.random() <= self.mutation_chance:
                index = random.randint(1, 3)
                newdna = DNA()
                if index == 1:
                    newdna.crouch_trigger = dino.dna.crouch_trigger
                    newdna.object_height_trigger = dino.dna.object_height_trigger
                elif index == 2:
                    newdna.jump_trigger = dino.dna.jump_trigger
                    newdna.object_height_trigger = dino.dna.object_height_trigger
                else:
                    newdna.jump_trigger = dino.dna.jump_trigger
                    newdna.crouch_trigger = dino.dna.crouch_trigger

    def mutate_diff(self, dinosaurs):
        """
        Allows Dinosaurs' DNA to mutate, but instead of mutating to a random value, just offset it a little bit from
        its old value
        @see mutate
        @param dinosaurs: the dinosaurs to mutate
        """
        for dino in dinosaurs:
            if random.random() <= self.mutation_chance:
                index = random.randint(1, 3)
                offset = random.randint(-10, 10)
                if index == 1:
                    dino.dna.jump_trigger += offset
                elif index == 2:
                    dino.dna.crouch_trigger += offset
                else:
                    dino.dna.object_height_trigger += offset

    def evolve(self):
        """
        Run the evolution:
            1. Perform natural selection
            2. Have fittest individuals mate
            3. Let babies mutate
            4. Create new population containing elitist, parents and babies
        This also increases the current_gen counter
        """
        sorted_dinos = sorted(self.dinosaurs, key=lambda x: x.score)
        if self.best_dinosaur.score < sorted_dinos[-1].score:
            self.best_dinosaur = sorted_dinos[-1]
        parents = self.select()[:]
        parents.append(self.best_dinosaur)  # elitist
        parents = [AIDinosaur.from_dinosaur(parent) for parent in parents]
        babies = self.mate(parents[:], self.n_population - len(parents))
        self.mutate_diff(babies)
        self.dinosaurs = parents + babies
        self.current_gen += 1
