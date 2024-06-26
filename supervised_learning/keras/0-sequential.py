#!/usr/bin/env python3

import tensorflow.keras as K

def build_model(nx, layers, activations, lambtha, keep_prob):
    model = K.models.Sequential()

    for i in range(len(layers)):
        model.add(Dense(units=layers[i] + 1, activation=activations[i], kernel_regularizer=K.regularizers.l2(lambtha)))
        if i < len(layers) - 1:
            model.add(Dropout(rate=keep_prob))

            model.compile(optimizer='adam', loss='mean_squared_error')

            return model