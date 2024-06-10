#!/usr/bn/env python3

import numpy as np

def shuffle_data(X, Y):
    assert len(X) == len(Y)
    p = np.random.permutation(len(X))
    return X[p], Y[p]