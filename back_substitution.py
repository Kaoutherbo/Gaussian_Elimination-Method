import numpy as np

def back_substitution(matrix, mat_size):
    
    sol_arr = np.zeros(mat_size)
    
    sol_arr[mat_size - 1] = (
        matrix[mat_size - 1][mat_size]
        / matrix[mat_size - 1][mat_size - 1]
    )

    for i in range(mat_size - 2, -1, -1):
        sol_arr[i] = matrix[i][mat_size]

        for j in range(i + 1, mat_size):
            sol_arr[i] = int(
                sol_arr[i] - matrix[i][j] * sol_arr[j]
            )

        sol_arr[i] = sol_arr[i] / matrix[i][i]

    return sol_arr
