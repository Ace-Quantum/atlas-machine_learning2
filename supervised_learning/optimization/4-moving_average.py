#!/usr/bin/env python3

"""documentation here"""

def moving_average(data, beta):
    """documentation here"""

    alpha = 1 - beta

    moving_averages = []

    if len(data) == 0:
        return moving_averages
    
    # n = sum((x - moving_averages[-1]) **2 for x in data)
    # d = len(data)
    # bias_correction_tem = n / d

    moving_averages.append(data[0])

    for i in range(1, len(data)):
        moving_average = alpha * data[i] + beta * moving_averages[-1]
        moving_averages.append(moving_average)

    n = len(data)
    d = len(moving_averages) -1
    bias_correction = n /d
    biased_moving_averages = [ma * bias_correction for ma in moving_averages]

    return biased_moving_averages