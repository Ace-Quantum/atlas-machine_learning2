#!/usr/bin/env python3

"""documentation here"""

def moving_average(data, beta):
    """documentation here"""

    moving_averages = []

    if len(data) == 0:
        return moving_averages
    
    full_weight = sum([i**(-beta) for i in range(1, len(data) + 1)])

    # moving_averages.append(data[0])

    exp_weighted_avg = 0

    for i in range(beta - 1, len(data)):
        weight_sum = sum([(i+1-j)**(-beta) * data[j] for j in range(i + 1)])
        moving_average = weight_sum / full_weight
        moving_averages.append(moving_average)
        

    return moving_averages