#!/usr/bin/env python3"""
"""A_prev is a numpy.ndarray of shape (
    m, h_prev, w_prev, c_prev) containing the output of the previous layer
        m is the number of examples
        h_prev is the height of the previous layer
        w_prev is the width of the previous layer
        c_prev is the number of channels in the previous layer
    kernel_shape is a tuple of (kh, kw)
      containing the size of the kernel for the pooling
        kh is the kernel height
        kw is the kernel width
    stride is a tuple of (sh, sw) containing the strides for the pooling
        sh is the stride for the height
        sw is the stride for the width
    mode is a string containing either max or avg,
      indicating whether to perform maximum or average pooling, respectively
    Returns: the output of the pooling layer"""
