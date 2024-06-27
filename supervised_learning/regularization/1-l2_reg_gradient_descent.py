#!/usr/bin/env python3
"""Here's some documentation
Y - one-hot numpy.ndarray of shape (classes, m)
    contains the correct labels for the data
classes - number of classes
m - number of data points
weights - dictionary of weights and biases of the neural network
cache - dictionary of outputs of each layer of the neural network
alpha - learning rate
lambtha - L2 regularization parameter
L - number of layers of the network"""

import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """And some more documentation"""

    grads = {}

    for i in range(L):
        z = cache['Z' + str(i+1)]
        a = cache['A' + str(i+1)]

        dz = a - Y
        dp = np.dot(cache['Z' + str(i)], dz.T)
        dW = dp / Y.shape[1] + lambtha * weights['W' + str(i+1)]
        db = np.sum(dz, axis=1, keepdims=True)

        grads['dW' + str(i+1)] = dW
        grads['db' + str(i+1)] = db

        if i != L - 1:
            da_prev = np.dot(weights['W' + str(i+2)].T, dz)
            cache['A' + str(i+2)] = np.tanh(da_prev)
            cache['Z' + str(i+2)] = da_prev

    for i in range(L):
        weights['W' + str(i+1)] -= alpha * grads['dW' + str(i+1)]
        weights['b' + str(i + 1)] -= grads['db' + str(i+1)]
