#!/usr/bin/env python3

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()

# create_placeholders = __import__('0-create_placeholders').create_placeholders
# create_layer = __import__('1-create_layer').create_layer

def create_layer(prev, n, activation):
    initializer = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    layer = tf.layers.Dense(units=n, activation=activation, kernel_initializer=initializer, name="layer")
    output = layer(prev)
    return output