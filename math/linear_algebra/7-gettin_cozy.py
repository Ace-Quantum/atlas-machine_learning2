#!/usr/bin/env python3

basic_matrix = __import__('6-howdy_partner').cat_arrays

def cat_matrices2D(mat1, mat2, axis=0):

    rows = len(mat1)
    cols = len(mat1[0])

    return_arr = [[0 for _ in range(cols)] for _ in range(rows)]


    if axis == 0:
        return (basic_matrix(mat1, mat2))
    else:
        return_arr[0] = basic_matrix(mat1[0], mat2[0])
        return_arr[1] = basic_matrix(mat1[1], mat2[1])
        return (return_arr)
