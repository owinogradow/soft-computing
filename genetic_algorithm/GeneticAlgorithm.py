from Population import Population
from Utils import fitnessFunction
import random
from matplotlib import pyplot as plt
import numpy as np
import sys
import copy

class GeneticAlgorithm:
    def __init__(self, popSize, amountOfGenerations, domain, granularity):
        self.amountOfGenerations = amountOfGenerations
        self.domain = domain
        self.popSize=popSize
        self.granularity = granularity
        self.population = Population(popSize, self.domain, self.granularity)
        self.crossoverProb = 0.8
        self.mutationProb = 0.01
        self.reproductionProb = 1 - self.crossoverProb - self.mutationProb
        self.results = {}
        
    def run(self):
        for generation in range(self.amountOfGenerations):
            for i in self.population.individuals:
                i.recalDecimalRepresentation()
            overallFitness = self.calculateFitness()
            self.results[generation] = overallFitness / len(self.population.individuals)
            self.calcChoosingProb(overallFitness)
            self.calcDistribuants()
            self.population.individuals = self.prepareNewPopulation()

        for i in self.population.individuals:
                i.recalDecimalRepresentation()
        xs = [ individual.repr for individual in self.population.individuals ]
        xs.sort()
        values = [ individual.fitness for individual in self.population.individuals ]
        values.sort()
        print("Found y={} for x0={}".format(values[-1], xs[-1]))
        plt.plot(list(self.results.keys()), list(self.results.values()))
        plt.show()

    def prepareNewPopulation(self):
        newPopulation = []
        while len(newPopulation) < self.popSize:
            operation = self.getOperationToExec()
            newIndividual = operation()
            if isinstance(newIndividual, tuple):
                newPopulation.extend(newIndividual)
            else:
                newPopulation.append(newIndividual)
        return newPopulation

    def performCrossover(self):
        indv1 = self.findIndividualByDistribuant()
        indv2 = self.findIndividualByDistribuant()
        crossoverIndex = random.randint(1, indv1.chromosomeSize - 1)
        firstPart1Chrom, secPart1Chrom = indv1.chromosome[:crossoverIndex], indv1.chromosome[crossoverIndex:]
        firstPart2Chrom, secPart2Chrom = indv2.chromosome[:crossoverIndex], indv2.chromosome[crossoverIndex:]
        indv1.chromosome = bin(int(firstPart1Chrom + secPart2Chrom,2))
        indv2.chromosome = bin(int(firstPart2Chrom + secPart1Chrom,2))
        return copy.copy(indv1), copy.copy(indv2)

    def performMutation(self):
        individual = self.findIndividualByDistribuant()
        bitToMutate = random.randint(0, individual.chromosomeSize-1)
        individual.chromosome = bin(int(individual.chromosome,2) ^ (1 << bitToMutate))
        return copy.copy(individual)

    def performReproduciton(self):
        individual = self.findIndividualByDistribuant()       
        return copy.copy(individual)

    def findIndividualByDistribuant(self):
        randDist = random.random()
        distribuants = [ individual.distribuant for individual in self.population.individuals ]
        distribuants.insert(0,0)
        for idx, individual in enumerate(self.population.individuals, 1):
            if distribuants[idx-1] < randDist and randDist <= distribuants[idx]:
                return individual

    def calculateFitness(self):
        overallFitness = 0
        for individual in self.population.individuals:
            individual.fitness = fitnessFunction(individual.repr)
            overallFitness += individual.fitness
        return overallFitness

    def calcChoosingProb(self, overallFitness):
        for individual in self.population.individuals:
            individual.choosingProbability = individual.fitness / overallFitness
    
    def calcDistribuants(self):
        distribuant = 0
        for individual in self.population.individuals:
            distribuant += individual.choosingProbability
            individual.distribuant = distribuant

    def getOperationToExec(self):
        operation = np.random.choice(a=[self.performCrossover, self.performMutation, self.performReproduciton],
                                    p=[self.crossoverProb, self.mutationProb, self.reproductionProb])
        return operation