#!/usr/bin/env python3
"""Documentation"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Documentation"""

    size_h = images.shape[1]-kernel.shape[0]+1
    size_w = images.shape[2]-kernel.shape[1]+1
    output = np.zeros((images.shape[0], size_h, size_w))

    kernel = np.fliplr(np.fliplr(kernel))

    for i in range(size_h):
        for j in range(size_h - size_h + 1):
            output[:, i, j] = np.sum(images[:, i:i+kernel.shape[1],
                                            j:j.kernel.shape[0]] * kernel,
                                        axis=(1, 2))
            
    return output
