#!/usr/bin/env python3

import numpy as np

def normalization_constants(X):
    norm_array = []
    diff_arr = np.amax(X) - np.amin(X)

    for i in X:
        temp = (i - np.min(X))/diff_arr
        norm_array.append(temp)

    mean_vals = np.mean(norm_array, axis=0)
    standard_vals = np.std(norm_array, axis=0)

    return mean_vals, standard_vals