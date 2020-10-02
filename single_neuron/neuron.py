import random

class Neuron:
    def __init__(self, numberOfInputs, numberOfEpochs, trainingStep, intervalWeights):
        self.numberOfInputs = numberOfInputs
        self.numberOfEpochs = numberOfEpochs
        self.trainingStep = trainingStep
        self.intervalWeights = intervalWeights
        self.initialWeights = [ random.uniform(intervalWeights[0], intervalWeights[1]) for _ in range(self.numberOfInputs) ]

    def train(self, trainingPatterns):
        for epoch in range(self.numberOfEpochs):
            for tp in trainingPatterns:
                predictedOutput = self.calculateOutput(tp.inputs)
                self.adjustWeights(tp.inputs, tp.output, predictedOutput)

    def calculateOutput(self, inputs):
        predOutput=0
        for x, w in zip(inputs, self.initialWeights):
            predOutput += x * w
        return predOutput

    def adjustWeights(self, inputs, desiredOutput, predictedOutput):
        for idx, (input, weight) in enumerate(zip(inputs, self.initialWeights)):
            self.initialWeights[idx] += self.trainingStep * (desiredOutput - predictedOutput) * input