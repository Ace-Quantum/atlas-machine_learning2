#!/usr/bin/env python3
"""Here's some documentation"""
import tensorflow as tf


def l2_reg_cost(cost, model):
    """And some more documentation"""
    l2_loss = tf.constant(0.0)

    for layer in model.layers:
        if layer.losses:
            l2_loss += tf.add_n(layer.losses)

    total_cost = cost + l2_loss

    return total_cost
