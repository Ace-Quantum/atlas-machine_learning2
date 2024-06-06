#!/usr/bin/env python3

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()

def calculate_accuracy(y, y_pred):
    y = tf.cast(y, tf.int32)
    y_pred = tf.argmax(y_pred, axis=1)

    correct_predictions = tf.equal(y, y_pred)

    accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))

    return accuracy