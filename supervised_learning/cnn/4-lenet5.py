#!/usr/bin/env python3

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

def lenet5(x, y):
    initializer = tf.keras.initializers.VarianceScaling(scale=2.0)

    conv1 = tf.layers.conv2d(x, filters=6, kernel_size=(5, 5),
                             padding='same', activation=tf.nn.relu, kernel_initializer=initializer)
    
    pool1 = tf.layers.max_pooling2d(conv1, pool_size=(2, 2), strides=(2, 2))

    conv2 = tf.layers.conv2d(pool1, filters=16, kernel_size=(5, 5),
                             padding='valid', activation=tf.nn.relu,
                             kernel_initializer=initializer)
    
    pool2 = tf.layers.max_pooling2d(conv2, pool_size=(2, 2), strides=(2, 2))

    flat = tf.layers.flatten(pool2)

    fc1 = tf.layers.dense(flat, units=120, activation=tf.relu, kernel_initializer=initializer)

    fc2 = tf.layers.dense(fc1, units=84, activation=tf.nn.relu, kernel_initializer=initializer)

    logits = tf.layers.dense(fc2, units=10, kernel_initialzer=initializer)
    softmax_output = tf.nn.softmax(logits)

    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=y))

    train_op = tf.train.AdamOptimizer().minimize(loss)

    correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    return softmax_output, train_op, loss, accuracy