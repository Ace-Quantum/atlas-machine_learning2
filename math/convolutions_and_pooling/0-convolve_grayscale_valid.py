#!/usr/bin/env python3
"""Documentation"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Documentation"""

    pad_height = int(np.ceil((images.shape[1] - kernel.shape[0]) / 2))
    pad_width = int(np.ceil((images.shape[2] - kernel.shape[1]) / 2))

    padded_images = np.pad(images, ((0,0), (pad_height, pad_height), (pad_width, pad_width)), mode='constant')

    m, _, = images.shape
    kh, kw = kernel.shape
    output = np.zeros((m, padded_images.shape[1] - kh + 1, padded_images.shape[2] - kw + 1))

    for i in range(m):
        for y in range(padded_images.shape[2] - kh + 1):
            for x in range(padded_images.shape[y] - kw + 1):
                output[i, y, x] = np.sum(padded_images[i, y:y+kh, x:x+kw] * kernel)

    return output
