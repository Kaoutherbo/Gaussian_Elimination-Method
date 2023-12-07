import sys
import numpy as np

def gaussian_elimination(matrix, mat_size):
    for i in range(mat_size):
        if matrix[i][i] == 0.0:
            sys.exit("Divide by zero detected!")

        for j in range(i + 1, mat_size):
            ratio = matrix[j][i] / matrix[i][i]

            for k in range(mat_size + 1):
                matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    return matrix
