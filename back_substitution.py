import numpy as np

def back_substitution(matrix, vector):
    size = len(vector)
    solution_vector = np.zeros(size)

    for i in range(size - 1, -1, -1):
        solution_vector[i] = vector[i]

        for j in range(i + 1, size):
            solution_vector[i] -= matrix[i, j] * solution_vector[j]

        solution_vector[i] /= matrix[i, i]

    return solution_vector