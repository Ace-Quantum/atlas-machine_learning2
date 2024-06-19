#!/usr/bin/env python3

"""Documentation"""
import numpy as np


def specificity(confusion):
    """documentation"""
    specificity_return = []
    num_classes = confusion.shape[0]
    # print("Num classes" + str(num_classes))

    for i in range(num_classes):
        true_neg = np.diag(confusion)
        false_pos = np.sum(confusion, axis=0) - true_pos

        specs = true_neg / (false_pos + false_neg) if false_neg > 0 else 1
        specificity_return.append(round(specs, 8))

    return specificity_return
