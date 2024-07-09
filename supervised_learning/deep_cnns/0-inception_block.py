#!/usr/bin/env python3
"""Builds an inception block"""

from tensorflow import keras as K


def inception_block(A_prev, filters):
    """Builds an inception block"""

    layer_1 = K.layers.Conv2D(
        filters=filters[0],
        kernel_size=(1, 1),
        padding='same',
        activation='relu'
    )(A_prev)

    # The resource has us redeclare layer_1. Why?
    # Also!!!! What the HECK does it mean putting the little dealiboop at the end?
    layer_1 = K.layers.Conv2D(
        filters=filters[1],
        kernel_size=(1, 1),
        padding='same',
        activation='relu'
    )(layer_1)

    layer_2 = K.layers.Conv2D(
        filters=filters[2],
        kernel_size=(3, 3),
        padding='same',
        activation='relu'
    )(A_prev)

    layer_2 = K.layers.Conv2D(
        filters=filters[3],
        kernel_size=(1, 1),
        padding = 'same',
        activation='relu'
    )(layer_2)

    layer_3 = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(1,1),
        padding='same'
    )(A_prev)

    layer_3 = K.layers.Conv2D(
        filters = filters[5],
        kernel_size=(1, 2),
        padding = 'same',
        activation = 'relu'
    )(layer_3)

    return K.layers.concatenate([layer_1, layer_2, layer_3], axis = 3)