#!/usr/bin/env python3

"""documentation here"""

def moving_average(data, beta):
    """documentation here"""

    moving_averages = []

    v_t = 0

    if len(data) == 0:
        return moving_averages
    
    # full_weight = sum([(i+1)**(-float_beta) for i in range(len(data))])

    for i in range(len(data)):
        v_t = beta * v_t + (1 - beta) * data[i]
        # weight_sum = sum([(i+1-j)**(-float_beta) * data[j] for j in range(int(beta), min(i+1, len(data) + 1))])
        # moving_average = weight_sum / full_weight
        moving_averages.append(v_t / (1 - beta**(i+1)))
        

    return moving_averages