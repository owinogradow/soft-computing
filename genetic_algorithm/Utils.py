import math

def fitnessFunction(arg):
    return (math.exp(arg) * math.sin(math.radians(10 * math.pi * arg)) + 1) / arg 