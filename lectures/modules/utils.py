import numpy as np

class RNG:
    def __init__(self, seed : int = 0):
        self.rng = np.random.default_rng(seed=seed)

    def generate(self, shape : tuple = None):
        # this is a bit silly because it only replicates the behaviour of random()
        # but this is just meant as an example
        if shape is not None:
            return self.rng.random(shape)
        else:
            return self.rng.random()