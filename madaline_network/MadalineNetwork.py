from ImageParser import ImageParser
from OutputNeuron import OutputNeuron
from InputNeuron import InputNeuron
import math

class MadalineNetwork:

    def __init__(self):
        self.iparser = ImageParser()
        self.inputNeurons = []
        self.outputNeurons = []

    def train(self, trainFile):
        trainImages = self.iparser.getTrainImages(trainFile)
        self.inputNeurons = [ InputNeuron() for _ in trainImages[0].pixels ]
        self.outputNeurons = [ OutputNeuron(list(self.normalizeImage(image.pixels)), image.value) for image in trainImages ]

    def predict(self, testFile):
        testImages = self.iparser.getTestImages(testFile)
        
        # iterating testing patterns
        for imageIdx, testImage in enumerate(testImages):
            
            # initializing input neurons
            for idx, pixel in enumerate(self.normalizeImage(testImage.pixels)):
                self.inputNeurons[idx] = pixel
            print("{} wzorzec testowy:".format(imageIdx +1))

            # creating comprehension dict with key equal to neuron 'label' and 
            # value equal to possibility that image contains neuron 'label'
            results = { outputNeuron.value : outputNeuron.calculateOutput(self.inputNeurons) for outputNeuron in self.outputNeurons }
            for neuron, value in results.items():
                print("neuron {} odpowiedział wartością {}".format(neuron, value))
            maxValue = max(results, key=results.get)
            print("Rozpoznano literę {} z prawdopodobieństwem {}".format(maxValue, results[maxValue]))
            
            

    def normalizeImage(self, pixels):
        amountOfOnes = pixels.count(1)
        return map((lambda value : value / math.sqrt(amountOfOnes) if value == 1 else value), pixels)