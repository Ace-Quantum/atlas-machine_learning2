#!/usr/bin/env python3

"""Documentation"""

import tensorflow.keras as K


def predict(network, data, verbose=True):
    """Documentation"""
    model = network
    predictions = model.predict(data)

    if verbose:
        print(predictions)

    return predictions
