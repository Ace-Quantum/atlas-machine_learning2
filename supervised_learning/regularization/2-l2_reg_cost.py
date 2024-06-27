#!/usr/bin/env python3
"""Here's some documentation"""
import tensorflow as tf


def l2_reg_cost(cost, model):
    """And some more documentation"""
    l2_loss = tf.constant(0., dtype=tf.float32)

    for layer in model.layers:
        if hasattr(layer, 'activity_regularizer'):
            l2_loss += tf.reduce_sum(
                layer.activity_regularizer.l2_regularization())

    total_cost = cost + l2_loss

    return total_cost
