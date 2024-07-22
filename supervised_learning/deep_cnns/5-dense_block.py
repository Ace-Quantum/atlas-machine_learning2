#!/usr/bin/env python3
"""Builds a dense block"""
"""This is code from a tutorial from
https://towardsdatascience.com/exploring-densenets-from-paper-to-keras-dcc01725488b"""

from tensorflow import keras as K

# I honestly don't know what I'm doing here anymore

def dense_block(X, nb_filters, growth_rate, layers):
    """Builds a dense block"""

    x = K.layers.BatchNormalization()(X)
    # x = K.layers.ReLU()(x)
    x = K.layers.Activation('relu')(x)


    num_filters_per_layer = []

    for i in range(layers):
        y = K.layers.Conv2D(filters=growth_rate * (i + 1),
                            kernel_size=3,
                            padding='same',
                            kernel_initializer=K.initializers.HeNormal(seed=0))(x)
        
        y = K.layers.BatchNormalization()(y)
        y = K.layers.Activation('relu')(y)

        x = K.layers.concatenate([x, y])

        num_filters_per_layer.append(growth_rate * (i + 1))

    return x, sum(num_filters_per_layer)
