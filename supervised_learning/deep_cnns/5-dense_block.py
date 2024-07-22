#!/usr/bin/env python3
"""Builds a dense block"""
"""This is code from a tutorial from
https://towardsdatascience.com/exploring-densenets-from-paper-to-keras-dcc01725488b"""

from tensorflow import keras as K

def H(inputs, filter_num, dropout):
    eps = 1.001e-5

    x = K.layers.BatchNormalization(epsilon=eps)(inputs)
    x = K.layers.Activation('relu')(x)
    x = K.layers.ZeroPadding2D((1, 1))(x)
    x = K.layers.Conv2D(filter_num, kernel_size=(3, 3), use_bias=False, kernel_initializer='he_normal')(x)
    x = K.layers.Dropout(rate=dropout)(x)
    return x

# def transition(inputs, filter_num, compression_factor, dropout):
#     eps = 1.001e-5
    
#     x = K.layers.BatchNormalization(epsilon=eps)(inputs)
#     x = K.layers.Activation('relu')(x)
#     num_feature_maps = inputs.shape[1]
    
#     filters = K.layers.Input(shape=(None, None, 1))
#     filters = K.layers.Lambda(
#         lambda x: K.floor_divide(K.cast(x, 'float32'), compression_factor
#                                  ))(filters)
    
#     # I'm not sure if I vibe with this line
#     filters = K.layers.Reshape((num_feature_maps,))(filters)

#     x = K.layers.Conv2D(
#         filters=filters, kernel_size=(1, 1), use_bias=False,
#         padding='same', kernel_initializer='he_normal',
#         kernel_regularizer=K.regularizers.l2(1e-4))(x)
    
#     x = K.layers.Dropout(dropout)(x)

#     x = K.layers.AveragePooling2D(pool_size=(2, 2))(x)

#     return x



def dense_block(X, nb_filters, growth_rate, layers):
    """Builds a dense block"""
    concat_features = X

    for _ in range(layers):
        bottleneck = K.layers.Conv2D(nb_filters, kernel_size=(1, 1), use_bias=False, kernel_initializer='he_normal')(concat_features)
        bottleneck = K.layers.BatchNormalization()(bottleneck)
        bottleneck = K.layers.Activation('relu')(bottleneck)

        new_features = H(bottleneck, growth_rate, 0.2)

        concat_features = K.layers.concatenate([concat_features, new_features])

        nb_filters += growth_rate

    return concat_features, nb_filters
