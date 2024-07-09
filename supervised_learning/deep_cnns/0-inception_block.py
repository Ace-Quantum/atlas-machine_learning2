#!/usr/bin/env python3
"""Builds an inception block"""

from tensorflow import keras as K


def inception_block(A_prev, filters):
    """Builds an inception block"""
