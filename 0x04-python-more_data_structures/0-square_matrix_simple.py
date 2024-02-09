#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = matrix.copy()
    con = 0
    for x in matrix2:
        x = list(map(lambda x: x * x, x))
        matrix2[con] = x
        con = con + 1
    return matrix2
