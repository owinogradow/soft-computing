import math

def sigmoid(output):
    return 1 / (1 + math.exp(-output))

def sigmoidDerivative(output):
    return sigmoid(output) * (1 - sigmoid(output))