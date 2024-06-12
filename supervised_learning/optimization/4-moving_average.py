#!/usr/bin/env python3

"""documentation here"""

def moving_average(data, beta):
    """documentation here"""

    alpha = 1 - beta

    moving_averages = []

    if len(data) == 0:
        return moving_averages

    moving_averages.append(data[0])

    for i in range(1, len(data)):
        moving_average = alpha * data[i] + beta * moving_averages[-1]
        moving_averages.append(moving_average)

    n = len(data)
    d = len(moving_averages)
    bias_correction = 1- beta**n
    biased_moving_averages = [ma / bias_correction for ma in moving_averages]

    return biased_moving_averages