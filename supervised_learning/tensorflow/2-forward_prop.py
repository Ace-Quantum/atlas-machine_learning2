#!/usr/bin/env python3

create_layer = __import__('1-create_layer').create_layer

def forward_prop(x, layer_sizes=[], activations=[]):
    prev_layer = x

    for size, activation in zip(layer_sizes, activations):
        prev_layer = create_layer(prev_layer, size, activation)

    return prev_layer
