#!/bin/usr/env python3

"""Documentation"""
import numpy as np


def f1_score(confusion):
    classes = confusion.shape[0]
    f1_scores = np.zeros(classes)

    sensitivity = __import__('1-sensitivity').sensitivity
    precision = __import__('2-precision').precision

    for i in range(classes):
        recall = sensitivity(confusion, i)

        prec = precision(confusion, i)

        if prec + recall == 0:
            f1_scores[i] = 0.0
        else:
            f1_scores[i] = 2 * (prec * recall) / (prec + recall)

    return f1_scores
