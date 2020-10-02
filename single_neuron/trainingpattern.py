import random

class TrainingPattern:
    def __init__(self, numberOfInputs, intervalInput):
        self.inputs = [ random.uniform(intervalInput[0], intervalInput[1]) for _ in range(numberOfInputs) ]
        self.output = random.uniform(intervalInput[0], intervalInput[1])