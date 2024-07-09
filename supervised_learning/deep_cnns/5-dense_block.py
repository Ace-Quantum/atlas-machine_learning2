#!/usr/bin/env python3
"""Builds a dense block"""

from tensorflow import keras as K


def dense_block(X, nb_filters, growth_rate, layers):
    """Builds a dense block"""
