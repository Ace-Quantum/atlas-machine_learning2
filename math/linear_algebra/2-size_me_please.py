#!/usr/bin/env python3

""" A program made to determine a shape """
""" I'm not sure what else they want here"""


def matrix_shape(matrix):
    if isinstance(matrix, list):
        return [len(matrix)] + matrix_shape(matrix[0])
    else:
        return []
