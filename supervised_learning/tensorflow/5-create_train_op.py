#!/usr/bin/env python3

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()

def create_train_op(loss, alpha):
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=alpha)
    train_op = optimizer.minimize(loss)

    return train_op
