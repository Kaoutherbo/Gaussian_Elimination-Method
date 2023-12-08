import numpy as np

def back_substitution(matrix, vector):
    size = len(vector)
    arr_sol = np.zeros(size)

    for i in range(size - 1, -1, -1):
        arr_sol[i] = vector[i]

        for j in range(i + 1, size):
            arr_sol[i] -= matrix[i, j] * arr_sol[j]

        arr_sol[i] /= matrix[i, i]

    return arr_sol
