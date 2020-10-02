from MadalineNetwork import MadalineNetwork

if __name__ == "__main__":
    madalineNetwork = MadalineNetwork()
    madalineNetwork.train("data/train_set.txt")
    madalineNetwork.predict("data/test_set.txt")