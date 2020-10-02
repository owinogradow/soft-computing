from InputNeuron import InputNeuron

class OutputNeuron:

    def __init__(self, normalizedPixels, value):
        self.weights = normalizedPixels
        self.value = value

    def calculateOutput(self, inputNeurons):
        output = 0
        for input, weight in zip(inputNeurons, self.weights):
            output += input * weight
        return output