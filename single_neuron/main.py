from neuron import Neuron
from trainingpattern import TrainingPattern

if __name__ == "__main__":
    print("{}  Single training pattern     {}".format("#"*20,"#"*20))
    neuron = Neuron(numberOfInputs=5, numberOfEpochs=1000, trainingStep=0.5, intervalWeights=(-1, 1))
    trainingPattern = TrainingPattern(5, (-1,1))
    neuron.train([trainingPattern])
    print("Actual output = {} neuron output after training process = {}".format(trainingPattern.output, neuron.calculateOutput(trainingPattern.inputs)))

    print("{}  Multiple training patterns  {}".format("#"*20,"#"*20))
    neuronMultiplePatterns = Neuron(5, 10000, 0.5, (-1, 1))
    trainingPatterns = [TrainingPattern(5, (-1,1)) for _ in range(5)]
    neuronMultiplePatterns.train(trainingPatterns)
    for tp in trainingPatterns:
        print("Actual output = {} neuron output after training process = {}".format(tp.output, neuronMultiplePatterns.calculateOutput(tp.inputs)))

        