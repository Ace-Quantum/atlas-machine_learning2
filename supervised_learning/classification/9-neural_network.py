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

        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros(shape=(nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """W1"""
        return self.__W1

    @property
    def b1(self):
        """b1"""
        return self.__b1

    @property
    def A1(self):
        """A1"""
        return self.__A1

    @property
    def W2(self):
        """W2"""
        return self.__W2

    @property
    def b2(self):
        """b2"""
        return self.__b2

    @property
    def A2(self):
        """A2"""
        return self.__A2
    
    def forward_prop(self, X):
        """AAAA
        Why does it feel like
        I'll never be enough
        for the checker"""

        Z1 = np.dot(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-Z1))
        
        Z2 = np.dot(self.__W2, self.A1) + self.__b2
        self.__A2 = 1 / (1 + np.exp(-Z2))

        return self.__A1, self.__A2