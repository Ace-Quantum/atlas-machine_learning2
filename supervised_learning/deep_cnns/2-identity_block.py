#!/usr/bin/env python3
"""Builds an identity block"""

from tensorflow import keras as K


def identity_block(A_prev, filters):
    """Builds an identity block"""
