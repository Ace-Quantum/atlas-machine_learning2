#!/usr/bin/env python3

import tensorflow as tf

def create_RMSProp_op(alpha, beta2, epsilon):

    return tf.keras.optimizers.RMSprop(learning_rate=alpha, rho=beta2, epsilon=epsilon)