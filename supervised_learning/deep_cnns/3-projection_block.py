#!/usr/bin/env python3
"""Builds a projection block"""

from tensorflow import keras as K


def projection_block(A_prev, filters, s=2):
    """Builds a projection block"""
