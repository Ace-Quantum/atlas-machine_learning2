#!/usr/bin/env python3

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()

def create_placeholders(nx, classes):
    X = tf.placeholder(tf.float32, shape=(None, nx), name="x")
    Y = tf.placeholder(tf.float32, shape=(None, classes), name="y")
    return X, Y