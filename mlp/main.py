from TrainingPattern import TrainingPattern
from MultiLayerPerceptron import MultiLayerPerceptron

if __name__ == "__main__":
    trainingPatterns = [ TrainingPattern([1,0,0,0], [1,0,0,0]),
                         TrainingPattern([0,1,0,0], [0,1,0,0]),
                         TrainingPattern([0,0,1,0], [0,0,1,0]),
                         TrainingPattern([0,0,0,1], [0,0,0,1]) ]
    mlp = MultiLayerPerceptron(inputLayerSize=4, hiddenLayersSize=[2], outputLayerSize=4, epochs=10000, learningStep=0.5, biasNeuron=True)
    mlp.train(trainingPatterns)
    
    for tp in trainingPatterns:
        out = mlp.calculateNetworkOutput(tp)
        print("Actual output : {} mlp returned : {}".format(tp.outputs, out))