#!/usr/bin/env python3

import tensorflow as tf

def create_momentum_op(alpha, beta1):
    global_step = tf.Variable(0)

    optimizer = tf.keras.optimizers.SGD(
        learning_rate=alpha, 
        momentum=beta1, 
        nesterov=True)

    return optimizer