#!/usr/bin/env python3

"""Documentation"""

import tensorflow.keras as K


def optimize_model(network, alpha, beta1, beta2):
    """Documentation"""

    adam_optomizer = K.optimizers.Adam(
        learning_rate=alpha,
        beta_1=beta1,
        beta_2=beta2)

    network.compile(
        loss="categorical_crossentropy",
        optimizer=adam_optomizer,
        metrics=["accuracy"]
    )

    return None
