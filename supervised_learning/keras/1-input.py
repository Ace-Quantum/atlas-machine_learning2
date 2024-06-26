#!/usr/bin/env python3

import tensorflow.keras as K

def build_model(nx, layers, activations, lambtha, keep_prob):
    inputs = K.layers.Input(shape=(nx,))

    x = inputs

    for i, num_nodes in enumerate(layers):
        x = K.layers.Dense(num_nodes, kernel_regularizer=l2(lambtha))(x)
        x = activations[i](x)

        if i < len(layers) - 1:
            x = K.layers.Dropout(keep_prob)(x)

    outputs = K.layers.Dense(layers[-1], activation='softmax')(x)

    model = Model(inputs=inputs, outputs=outputs)

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model