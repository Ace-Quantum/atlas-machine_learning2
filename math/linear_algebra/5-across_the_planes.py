#!/usr/bin/env python3

size_matrix = __import__('2-size_me_please').matrix_shape

def add_matrices2D(mat1, mat2):

    rows = len(mat1)
    cols = len(mat1[0])

    return_arr = [[0 for _ in range(rows)] for _ in range(cols)]
    
    if size_matrix(mat1) != size_matrix(mat2):
        return (None)
    
    for i in range(rows):
        for j in range(cols):
            return_arr[i][j] = mat1[i][j] * mat2[i][j]

    return (return_arr)
