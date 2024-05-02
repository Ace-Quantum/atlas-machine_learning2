#!/usr/bin/env python3

basic_matrix_cat = __import__('6-howdy_partner').cat_arrays
size_matrix = __import__('2-size_me_please').matrix_shape


def cat_matrices2D(mat1, mat2, axis=0):

    rows = len(mat1)
    cols = len(mat1[0])

    return_arr = [[0 for _ in range(cols)] for _ in range(rows)]

    if len(mat1) == 0 or len(mat1[0]) == 0:
        return return_arr
    
    if len(mat2) == 0 or len(mat2[0]) == 0:
        return return_arr

    if len(size_matrix(mat1)) != len(size_matrix(mat2)):
        return (None)
    elif axis == 0:
        return (basic_matrix_cat(mat1, mat2))
    else:
        return_arr[0] = basic_matrix_cat(mat1[0], mat2[0])
        return_arr[1] = basic_matrix_cat(mat1[1], mat2[1])
        return (return_arr)
