from InputNeuron import InputNeuron
from Neuron import Neuron
import random
import numpy as np

class MultiLayerPerceptron:
    def __init__(self, inputLayerSize, hiddenLayersSize, outputLayerSize, epochs, learningStep=0.5, biasNeuron=False):
        self.learningStep = learningStep
        self.bias = biasNeuron
        if biasNeuron:
            self.biasNeuron = InputNeuron(1)
        self.inputLayer = [ InputNeuron() for _ in range(inputLayerSize) ]
        
        self.hiddenLayers = []
        # populate first hidden layer
        self.hiddenLayers.append( [ Neuron(inputLayerSize + int(self.bias)) for _ in range(hiddenLayersSize.pop(0)) ] )

        # we allow to pass multiple hidden layers
        for idx, hiddenLayerSize in enumerate(hiddenLayersSize):
            self.hiddenLayers.append( [ Neuron(len(self.hiddenLayers[idx]) + int(self.bias)) for _ in range(hiddenLayerSize) ] )
        self.outputLayer = [ Neuron(len(self.hiddenLayers[-1]) + int(self.bias)) for _ in range(outputLayerSize) ]
        self.layers = [ self.inputLayer, *self.hiddenLayers, self.outputLayer ]
        self.epochs = epochs
        
    def calculateNetworkOutput(self, tp):
        # initialize input neurons
        for inputNeuron, inpt in zip(self.inputLayer, tp.inputs):
            inputNeuron.output = inpt
        # calculate output values for layers
        # omit input layer, no need to calc outputs there
        for idx, layer in enumerate(self.layers[1:]):
            for neuron in layer:
                inputs = [ neuron.output for neuron in self.layers[idx] ]
                if self.bias:
                    inputs.append(self.biasNeuron.output)
                neuron.calcOutput( inputs )
        if self.bias:
            outputs = []
            outputs.append([ neuron.output for neuron in self.layers[-1] ])
            for hiddenLayer in self.hiddenLayers[::-1]:
                outputs.append([ neuron.output for neuron in hiddenLayer ])
            return outputs
        else:
            return [ neuron.output for neuron in self.layers[-1] ]

    def train(self, trainingPatterns):
        random.shuffle(trainingPatterns)
        for epoch in range(self.epochs):
            for tp in trainingPatterns:
                self.calculateNetworkOutput(tp)

                # calculate error signal for the output layer
                for neuron, output in zip(self.layers[-1], tp.outputs):
                    neuron.calcErrorSignal(tpOutput=output)
                # calculate error signals for layers from last but one
                for idx, layer in enumerate(self.layers[-2:0:-1]):
                    for neuronIdx, neuron in enumerate(layer):
                        weightedSum = np.dot(
                            a=[ neuronInNextLayer.weights[neuronIdx] for neuronInNextLayer in self.layers[-idx-1] ],
                            b=[ neuronInNextLayer.errorSignal for neuronInNextLayer in self.layers[-idx-1] ])
                        neuron.calcErrorSignal(weightedSumErrorSig=weightedSum)

                # adjust weights
                for layerIdx, layer in enumerate(self.layers[1:]):
                    for neuron in layer:
                        if self.bias:
                            for weightIdx, weight in enumerate(neuron.weights[:-1]):
                                neuron.weights[weightIdx] += self.learningStep * neuron.errorSignal * self.layers[layerIdx][weightIdx].output
                            neuron.weights[-1] += self.learningStep * neuron.errorSignal * self.biasNeuron.output
                        else:
                            for weightIdx, weight in enumerate(neuron.weights):
                                neuron.weights[weightIdx] += self.learningStep * neuron.errorSignal * self.layers[layerIdx][weightIdx].output
