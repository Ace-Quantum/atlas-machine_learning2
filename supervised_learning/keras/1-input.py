#!/usr/bin/env python3
"""Documentation"""

import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """Documentation"""
    inputs = K.layers.Input(shape=(nx,))

    x = inputs

    for i in range(len(layers) - 1):
        x = K.layers.Dense(
            layers[i],
            kernel_regularizer=K.regularizers.l2(lambtha),
            activation=activations[i],
        )(x)
        x = K.layers.Dropout(keep_prob)(x)

        if i < len(layers) - 1:
            x = K.layers.Dropout(keep_prob)(x)

    outputs = K.layers.Dense(layers[-1], activation="softmax")(x)

    model = K.models.Model(inputs=inputs, outputs=outputs)

    return model
