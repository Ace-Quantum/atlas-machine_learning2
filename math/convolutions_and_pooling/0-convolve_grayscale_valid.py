#!/usr/bin/env python3
"""Documentation"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Documentation"""

    m, h, w = images.shape
    kh, kw = kernel.shape
    output = np.zeros((m, h - kh + 1, w - kw + 1))

    kernel = np.fliplr(np.fliplr(kernel))

    for i in range(m):
        for j in range(h - kh + 1):
            for k in range(w - kw + 1):
                output[i, j, k] = np.sum(images[i, j:j+kh, k:k+kw] * kernel)

    return output
