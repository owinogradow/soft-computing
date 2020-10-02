from functools import reduce
from Utils import sigmoid, sigmoidDerivative
import random
import numpy as np

class Neuron:

    def __init__(self, amountOfInputs):
        self.weights = [ random.uniform(-0.5, 0.5) for _ in range(amountOfInputs) ]
        self.output = 0
        self.weightedSum = 0
        self.errorSignal = 0

    def calcOutput(self, inputs):
        self.weightedSum = np.dot(inputs, self.weights)
        self.output = sigmoid(self.weightedSum)
        return self.output

    def calcErrorSignal(self, tpOutput=None, weightedSumErrorSig=None):
        if tpOutput is not None:
            self.errorSignal = sigmoidDerivative(self.weightedSum) * (tpOutput - self.output)
        elif weightedSumErrorSig is not None:
            self.errorSignal = sigmoidDerivative(self.weightedSum) * weightedSumErrorSig
        else:
            raise AttributeError("Wrong parameter passed")