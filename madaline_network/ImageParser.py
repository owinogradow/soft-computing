import re
from Image import Image

class ImageParser:
    def __init__(self):
        pass

    def getTrainImages(self, trainingFile):
        trainImages = []
        content = []
        with open(trainingFile, "rt") as trainingSetFile:
            content = trainingSetFile.readlines()
        # remove comments, strip newlines chars
        content = [ line.split(";")[0].strip() for line in content if not line.startswith(";") ]
        amountOfPxInCol = int(content.pop(2))
        ammountOfPxInRow = int(content.pop(1))
        amountOfImages = int(content.pop(0))
        for idx in range(amountOfImages):
            value = content.pop(0)
            pixels = []
            for rows in range(ammountOfPxInRow):
                #split one 4 char string into 4 strings
                for char in list(content.pop(0)):
                    pixels.append(char)
            trainImages.append(Image(pixels,value))
        return trainImages
        
    def getTestImages(self, testFile):
        testImages = []
        content = []
        with open(testFile, "rt") as testingSetFile:
            content = testingSetFile.readlines()
        content = [ line.split(";")[0].strip() for line in content if not line.startswith(";") ]
        amountOfPxInCol = int(content.pop(2))
        ammountOfPxInRow = int(content.pop(1))
        amountOfImages = int(content.pop(0))
        for idx in range(amountOfImages):
            pixels = []
            for rows in range(ammountOfPxInRow):
                #split one 4 char string into 4 strings
                for char in list(content.pop(0)):
                    pixels.append(char)
            testImages.append(Image(pixels))
        return testImages