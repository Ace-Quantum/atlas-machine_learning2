#!/usr/bin/env python3
"""Builds an inception block"""

from tensorflow import keras as K


def inception_block(A_prev, filters):
    """Builds an inception block"""

    layer_1 = K.layers.convolutional.Conv2D(
        layers=filters[0],
        kernel_size=(1, 1),
        padding='same',
        activation='relu'
    )

    return layer_1
