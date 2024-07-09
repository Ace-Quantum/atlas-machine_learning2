#!/usr/bin/env python3
"""Builds the DenseNet-121 architecture"""

from tensorflow import keras as K


def densenet121(growth_rate=31, compression=1.0):
    """Builds the DenseNet architecture"""
