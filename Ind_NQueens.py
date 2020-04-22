"""
Author: Alejandro Arbelaez (Alejandro.Arbelaez@cit.ie)
Math example
file: Individual.py
"""



import random
import math

class Individual:
    def __init__(self, _size):
        """
        Parameters and general variables
        """
        self.fitness = 0
        self.genes   = []
        self.genSize = _size

        for i in range(0, self.genSize):
            self.genes.append( random.randint(0, 1))
            
        self.genes = [i for i in range(1, self.genSize + 1)]
        for i in range(0, self.genSize):
            n1 = random.randint(0, self.genSize-1)
            n2 = random.randint(0, self.genSize-1)
            tmp = self.genes[n2]
            self.genes[n2] = self.genes[n1]
            self.genes[n1] = tmp

    def getFitness(self):
        return self.fitness


    def computeFitness(self):
        """
        Current fitness value.
        +1 if another Queen on same row
        +1 if another Queen on sam diagonal
        """
        self.fitness = 0
        for i in range(0, self.genSize):
            for j in range(1, self.genSize):
                if i == j:
                    continue
                #if self.genes[i] == self.genes[j]:
                #    self.fitness += 1
                if abs(self.genes[i] - self.genes[j]) == abs(i - j):
                    self.fitness += 1
                

    def copy(self):
        """
        Cloning this object
        """
        ind = Individual(self.genSize)
        for i in range(0, self.genSize):
            ind.genes[i] = self.genes[i]
        return ind

