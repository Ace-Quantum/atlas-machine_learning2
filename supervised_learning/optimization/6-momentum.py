#!/usr/bin/env python 3

import tensorflow as tf

def create_momentum_op(alpha, beta1):
    global_step = tf.Variable(0)

    optimizer = tf.train.MomentumOptimizer(alpha, beta1, use_nesterov=True)

    loss_func = tf.losses.mean_squared_error()
    train_op = optimizer.minimize(loss_func, global_step=global_step)

    return train_op