#!/usr/bin/env python3
"""Builds an inception network"""

from tensorflow import keras as K
inception_block = __import__('0-inception_block').inception_block


def inception_network():
    """Builds an inception block"""

    model = K.models.Sequential()

    model.add(
        K.layers.Conv2D(
            kernel_size=(7, 7),
            padding='same',
            activation='relu'
        )
    )

    model.add(
        K.layers.MaxPooling2D(
            pool_size=(3, 3),
            strides=(2, 2),
            padding='same'
        )
    )

    model.add(
        K.layers.Conv2D(
            kernel_size=(1, 1),
            padding='same',
            activation='relu'
        )
    )

    model.add(
        K.layers.Conv2D(
            kernel_size=(3, 3),
            padding='same',
            activation='relu'
        )
    )

    model.add(
        K.layers.MaxPooling2D(
            pool_size=(3, 3),
            strides=(2, 2),
            padding='same'
        )
    )

    model.add(inception_block(model.layers[-1], [64, 96, 128, 16, 32, 32]))

    model.add(inception_block(model.layers[-1], [128, 128, 192, 32, 96, 64]))

    model.add(
        K.layers.MaxPooling2D(
            pool_size=(3, 3),
            strides=(2, 2),
            padding='same'
        )
    )

    model.add(inception_block(model.layers[-1], [128, 128, 192, 32, 96, 64]))
