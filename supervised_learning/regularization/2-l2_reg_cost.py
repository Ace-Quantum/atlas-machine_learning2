#!/usr/bin/env python3
"""Here's some documentation"""
import tensorflow as tf


def l2_reg_cost(cost, model):
    """And some more documentation"""
    l2_loss = tf.constant(0.0)
    layer_losses = []

    for layer in model.layers:
        if isinstance(layer, tf.keras.layers.Dense):
            l2_loss += tf.reduce_sum(layer.losses)

    total_cost = cost + layer_losses

    return total_cost
