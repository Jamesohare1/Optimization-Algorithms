
"""
Author: Alejandro Arbelaez (Alejandro.Arbelaez@cit.ie)
Monkey example
file: Example.py
"""

import random
from Ind_NQueens import *


class GA:

    def __init__(self, _popSize, _genSize, _mutationRate, _maxIterations):
        """
        Parameters and general variables
        """
        self.population     = []
        self.matingPool     = []
        self.best           = None
        self.popSize        = _popSize
        self.genSize        = _genSize
        self.mutationRate   = _mutationRate
        self.maxIterations  = _maxIterations
        self.iteration      = 0
        self.initPopulation()

    def initPopulation(self):
        """
        Creating the initial population (random values)
        """
        for i in range(0, self.popSize):
            individual = Individual(self.genSize)
            individual.computeFitness()
            self.population.append(individual)
        self.best = self.population[0]

    def randomSelection(self):
        """
        Random (uniform) selection of two individuals
        """
        indA = self.matingPool[ random.randint(0, self.popSize-1) ]
        indB = self.matingPool[ random.randint(0, self.popSize-1) ]
        return [indA, indB]

    def crossover(self, indA, indB):
        """
        Executes a one point crossover and returns a new individual
        :param ind1: The first parent (or individual)
        :param ind2: The second parent (or individual)
        :returns: A new individual
        """
        child1 = indA.copy()
        child2 = indB.copy()

        #STEP 1
        #Randomly select positions that will no longer change
        selection = [random.randint(0,1) for i in range(0, self.genSize)]
        child1.genes = [a*b for a,b in zip(child1.genes, selection)]
        child2.genes = [a*b for a,b in zip(child2.genes, selection)]
        
        unused1 = [num for num in indB.genes if num not in child1.genes]
        unused2 = [num for num in indA.genes if num not in child2.genes]
       
        #STEP 1
        #Populate remaining genes
        for i in range(0, self.genSize):
            if child1.genes[i] == 0:
                child1.genes[i] = unused1.pop()
                child2.genes[i] = unused2.pop()
                
        
        return(child1, child2)


    def updateBest(self, candidate):
        """
        updating the best individual observed so far
        """
        if candidate.getFitness() < self.best.getFitness():
            self.best = candidate
            print ("Best: ", self.best.getFitness()," iterations: ",self.iteration)

    def newGeneration(self):
        """
        Creating a new generation
        1. Selection
        2. Crossover
        3. Mutation
        """
        for i in range(0, int(len(self.population) / 2)):
            #matingPool = self.selection()
            #[ind1, ind2] = self.randomSelection()
            [ind1, ind2] = self.randomSelection()
            child1, child2 = self.crossover(ind1, ind2)
            self.mutation(child1)
            self.mutation(child2)
            self.population[i] = child1
            self.population[i+1] = child2

    def mutation(self, candidate):
        gene1 = random.randint(0, self.genSize - 1)
        gene2 = random.randint(0, self.genSize - 1)
        
        temp = candidate.genes[gene1]
        candidate.genes[gene1] = candidate.genes[gene2]
        candidate.genes[gene1] = temp
        candidate.computeFitness()
        self.updateBest(candidate)

    def printPopulation(self):
        for ind_i in self.population:
            print (ind_i.genes, ind_i.getFitness())

    def updateMatingPool(self):
        """
        Updating the mating pool before creating a new generation
        """
        self.matingPool = []
        for ind_i in self.population:
            self.matingPool.append( ind_i.copy() )

    def GAStep(self):
        """
        One step in the GA main algorithm
        1. Computing Fitness for each candidate in the population
        2. Updating mating pool with current population
        3. Creating a new Generation
        """
        for ind_i in self.population:
            ind_i.computeFitness()
        self.updateMatingPool()
        self.newGeneration()

    def search(self):
        """
        General search template.
        Iterates for a given number of iterations
        """

        self.iteration = 0
        while self.iteration < self.maxIterations and self.best.getFitness() > 0:
            self.GAStep()
            self.iteration += 1
        print ("Total iterations: ", self.iteration)
        print ("Best solution: ",self.best.getFitness())

ga = GA(50, 16, 0.01, 10000)
ga.search()

#for gene in ga.population:
#print(gene.genes)
#print(gene.fitness)
    
