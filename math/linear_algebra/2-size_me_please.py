#!/usr/bin/env python3

# A program made to determine a shape
def matrix_shape(matrix):
    # Some more documentation
    if isinstance(matrix, list):
        return [len(matrix)] + matrix_shape(matrix[0])
    else:
        return []
