import numpy as np

def back_substitution(matrix, vector_b):
    mat_size = len(vector_b)
    arr_sol = np.zeros(mat_size)

    for i in range(mat_size - 1, -1, -1):
        S = np.dot(matrix[i, i+1:], arr_sol[i+1:])
        arr_sol[i] = (vector_b[i] - S) / matrix[i, i]

    return arr_sol