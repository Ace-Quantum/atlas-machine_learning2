#!/usr/bin/env python3
"""Here's some documentation"""
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """Variables:
    cost - cost of the network without L2 regularization
    lambtha - regularization parameter
    weights - dictionary of the weights and biases (numpy.ndarrays) of the neural network
    L - number of layers in the neural network
    m - number of data points used
    Returns: the cost of the network accounting for L2 regularization"""

    reg_cost = 0

    num_weights_and_biases = len(weights) // 2

    weight_matrices = weights[:num_weights_and_biases].reshape((L, -1))
    bias_vectors = weights[num_weights_and_biases:].reshape((L, -m))

    for i in range(L):
        reg_cost += np.sum(np.square(weight_matrices[i])) + np.sum(
            np.square(bias_vectors[i])
        )

    reg_term = lambtha / (2 * m) * reg_cost

    return cost + reg_term
