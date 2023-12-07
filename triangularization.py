import sys
import numpy as np


def triangularization(matrix, vector_b):
    mat_size = len(vector_b)

    for k in range(mat_size - 1):
        for i in range(k + 1, mat_size):
            w = matrix[i, k] / matrix[k, k]
            for j in range(mat_size):
                if j < k:
                    matrix[i, j] = 0
                else:
                    matrix[i, j] -= w * matrix[k, j]
            vector_b[i] -= w * vector_b[k]

    return matrix, vector_b