#!/usr/bin/env python3

basic_matrix_cat = __import__('6-howdy_partner').cat_arrays
size_matrix = __import__('2-size_me_please').matrix_shape

def cat_matrices2D(mat1, mat2, axis=0):

    # if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        # return (None)

    # if len(size_matrix(mat1)) != len(size_matrix(mat2)):
        # return (None)
    # print ("len of mat1[0]: " + str(len(mat1[0])))
    # print ("len of mat2[0]: " + str(len(mat2[0])))

    if axis == 0 and len(mat1) != len(mat2):
        return (None)
    if axis == 1 and len(mat1[0]) != len(mat2[0]):
        return (None)

    return_arr = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]

    if axis == 0:
        return (basic_matrix_cat(mat1, mat2))
    else:
        return_arr[0] = basic_matrix_cat(mat1[0], mat2[0])
        return_arr[1] = basic_matrix_cat(mat1[1], mat2[1])
        return (return_arr)    
