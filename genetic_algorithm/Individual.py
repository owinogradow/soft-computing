import random

class Individual:
    def __init__(self, domain, granularity):
        self.domain = domain
        self.granularity = granularity
        self.chromosomeSize = self.findChromosomeSize()
        self.chromosome = bin(random.getrandbits(self.chromosomeSize))
        self.repr = None
        self.fitness = None
        self.choosingProbability = None
        self.distribuant = None

    def findChromosomeSize(self):
        exponent = 1
        while(True):
            if (self.domain[1] - self.domain[0]) * 10 **self.granularity < 2 ** exponent -1:
                return exponent
            else:
                exponent += 1

    def recalDecimalRepresentation(self):
        repr = round(self.domain[0] + int(self.chromosome, 2)*(self.domain[1] - self.domain[0]) / (2**self.chromosomeSize - 1), 3)
        self.repr = repr

    def bits(self, n):
        while n:
            b = n & (~n+1)
            yield b
            n ^= b
