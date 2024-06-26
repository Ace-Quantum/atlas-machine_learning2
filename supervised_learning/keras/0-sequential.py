#!/usr/bin/env python3
"""Documentation"""

import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """Documentation"""
    shape = (None, nx)
    model = K.models.Sequential([
        K.layers.Input(shape=shape[1:])
    ])

    for i in range(len(layers)):
        model.add(
            K.layers.Dense(
                units=layers[i] + 1,
                activation=activations[i],
                kernel_regularizer=K.regularizers.l2(lambtha),
            )
        )
        if i < len(layers) - 1:
            model.add(K.layers.Dropout(rate=keep_prob))

    model.compile(optimizer="adam", loss="mean_squared_error")

    return model
