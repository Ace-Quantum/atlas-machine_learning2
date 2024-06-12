#!/usr/bin/env python3

import tensorflow as tf

def create_momentum_op(alpha, beta1):
    global_step = tf.Variable(0)

    optimizer = tf.train.MomentumOptimizer(alpha, beta1, use_nesterov=True).minimize(tf.losses.mean_squared_error(), global_step=global_step)

    return optimizer