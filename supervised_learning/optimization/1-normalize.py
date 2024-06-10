#!/usr/bin/env python3

import numpy as np

def normalize(X, m, s):
    norm_arr = []

    for i in X:
        temp = i / X.max()
        norm_arr.append(temp)

    return norm_arr
