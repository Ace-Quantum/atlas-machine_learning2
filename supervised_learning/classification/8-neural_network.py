#!/usr/bin/env python3

"""Building the network itself"""

import numpy as np

"""Idk I'm just putting documentation everywhere"""


class NeuralNetwork:
    """One day AI will take over the world.
    Let's hope they're nice about it"""

    def __init__(self, nx, nodes):
        """crickets"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.W1 = np.random.normal(size=(nodes, nx))
        self.b1 = np.zeros(shape=(nodes, 1))
        self.A1 = 0
        self.W2 = np.random.normal(size=(1, nodes))
        self.b2 = 0
        self.A2 = 0
