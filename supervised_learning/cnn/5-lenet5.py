#!/usr/bin/env python3

from tensorflow import keras as K
from tensorflow.keras import layers, models, initializers

def lenet5(X):
    initializer = initializers.he_normal(seed=0)

    conv1 = layers.Conv2D(6, (5, 5), padding='same',
                          kernel_initializer=initializer, activation='relu')(X)
    
    pool1 = layers.MaxPooling2D((2, 2), strides=(2, 2))(conv1)

    conv2 = layers.Conv2D(16, (5, 5), padding='valid',
                          kernel_initializer=initializer, activation='relu')(pool1)
    
    pool2 = layers.MaxPooling2D((2, 2), strides=(2,2))(conv2)

    flat = layers.Flatten()(pool2)

    fc1 = layers.Dense(120, kernel_initializer=initializer,
                       activation='relu')(flat)
    
    fc2 = layers.Dense(84, kernel_initializer=initializer,
                       activation='relu')(fc1)
    
    output = layers.Dense(10, kernel_initializer=initializer,
                          activation='softmax')(fc2)
    
    model = models.Model(inputs=X, outputs=output)

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model