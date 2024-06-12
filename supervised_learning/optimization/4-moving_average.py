#!/usr/bin/env python3

"""documentation here"""

def moving_average(data, beta):
    """documentation here"""

    alpha = 1 - beta

    moving_averages = []

    if len(data) > 0:
        moving_averages.append(data[0])
    else:
        return moving_averages
    
    n = sum((x - moving_averages[-1]) **2 for x in data)
    d = len(data)
    bias_correction_tem = n / d

    for i in range(1, len(data)):
        moving_average = alpha * data[i] + (1 - alpha) * moving_averages[i - 1] + bias_correction_tem
        moving_averages.append(moving_average)

    return moving_averages