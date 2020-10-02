class Image:

    stringToBinary = {
        "#" : 1,
        "-" : 0
    }

    def __init__(self, pixels, value = None):
        self.pixels = [ Image.stringToBinary.get(char) for char in pixels]
        self.value = value