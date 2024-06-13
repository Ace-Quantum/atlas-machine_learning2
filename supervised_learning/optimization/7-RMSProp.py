#!/usr/bin/env python3

def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    s_new = beta2 * s + (1 - beta2) * (grad ** 2)

    var_new = var - alpha * grad / np.sqrt(s_new + epsilon)

    return var_new, s_new