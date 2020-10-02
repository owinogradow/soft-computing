from GeneticAlgorithm import GeneticAlgorithm

if __name__=='__main__':
    ga = GeneticAlgorithm(popSize=100, amountOfGenerations=500, domain=(0.5,2.5), granularity=3)
    ga.run()