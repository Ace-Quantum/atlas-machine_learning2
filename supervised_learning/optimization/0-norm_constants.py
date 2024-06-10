#!/usr/bin/env python3

import numpy as np

def normalization_constants(X):

    # norm_X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

    mean_vals = np.mean(X, axis=0)
    standard_vals = np.std(X, axis=0)

    return mean_vals, standard_vals


    # norm_arr = []
    # for i in X:
    #     temp = i / X.max()
    #     norm_arr.append(temp)



    # diff_arr = np.max(X) - np.min(X)

    # norm_array = ((X - X.min()) / diff_arr)
