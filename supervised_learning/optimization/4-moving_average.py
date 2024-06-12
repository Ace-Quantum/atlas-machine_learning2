#!/usr/bin/env python3

"""documentation here"""

def moving_average(data, beta):
    """documentation here"""

    alpha = 1 - beta

    moving_averages = []

    if len(data) == 0:
        return moving_averages

    # moving_averages.append(data[0])

    exp_weighted_avg = 0

    for i in range(1, len(data)):
        exp_weighted_avg = beta * exp_weighted_avg + alpha * data[i]
        bias = 1 - beta**(i + 1)
        moving_averages.append(exp_weighted_avg / bias)

    return moving_averages