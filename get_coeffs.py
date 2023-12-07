import numpy as np

def get_coeffs(mat_size):
    matrix = np.zeros((mat_size, mat_size + 1))
    
    for i in range(mat_size):
        for j in range(mat_size + 1):
            matrix[i][j] = float(input(f"a[{i}][{j}] = "))
    return matrix
