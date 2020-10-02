from Individual import Individual

class Population:
    def __init__(self, size, domain, granularity):
        self.size = size
        self.individuals = [ Individual(domain, granularity) for _ in range(size) ]