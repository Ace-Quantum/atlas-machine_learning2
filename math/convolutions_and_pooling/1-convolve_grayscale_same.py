#!/usr/bin/env python3
"""Documentation"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Documentation"""

    m, h, w = images.shape
    kh, kw = kernel.shape

    pad_h = (h - 1) // 2
    pad_w = (w - 1) // 2

    pad_images = np.pad(images, ((0, 0), (pad_h, pad_h), (
        pad_w, pad_w)), mode='constant')

    con_images = np.zeros((m, h, w))

    for i in range(h):
        for j in range(w):
            con_images[:, i, j] = np.sum(
                pad_images[:, i:i+kh, j:j+kw] * kernel, axis=(1, 2)
            )

    return con_images
