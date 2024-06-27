#!/usr/bin/env python3
"""Documentation"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Documentation"""

    m, h, w = images.shape
    kh, kw = kernel.shape

    out_h = h - kh + 1
    out_w = w - kw + 1

    print(f"Images shape: {images.shape}")
    print(f"Kernel shape: {kernel.shape}")
    print(f"Output shape: (m, {out_h}, {out_w})")

    output = np.zeros((m, out_h, out_w))

    for i in range(m):
        for y in range(out_h):
            for x in range(out_w):
                output[i, y, x] = np.sum(images[i, y:y+kh, x:x+kw] * kernel)

    return output
