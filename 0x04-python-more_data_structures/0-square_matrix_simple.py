#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[0 for j in range(len(matrix[0]))] for i in range(matrix)]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[i][j] = matrix[i][j] * matrix [i][j]

    return (new_matrix)
