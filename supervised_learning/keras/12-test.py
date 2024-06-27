#!/usr/bin/env python3

"""Documentation"""

import tensorflow.keras as K


def test_model(network, data, labels, veerbose=True):
    """Documentation"""
    model = network
    return model.evaluate(data, labels, verbose=veerbose)
