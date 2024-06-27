#!/usr/bin/env python3

"""Documentation"""

import tensorflow.keras as K


def save_config(network, filename):
    """Documentation"""
    config = network.to_json()
    with open(filename, 'w') as json_file:
        json_file.write(config)


def load_configuration(filename):
    """Documentation"""
    with open(filename, 'r') as json_file:
        config = json_file.read()
    model = K.models.model_from_json(config)
    return model
