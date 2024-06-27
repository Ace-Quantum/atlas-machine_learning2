#!/usr/bin/env python3
"""Documentation"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Documentation"""

    size_h = images.shape[1]-kernel.shape[0]+1
    size_w = images.shape[2]-kernel.shape[1]+1
    output = np.zeros((images.shape[0], size_h, size_w))

    kernel = np.flipud(np.fliplr(kernel))

    for i in range(images.shape[0]):
        for j in range(size_h):
            for k in range(size_w):
                sub_output = images[i, j:j+kernel.shape[0], k:k+kernel.shape[1]]
                output[:, i, j] = np.sum(sub_output * kernel)
            
    return output
