import numpy as np

def get_coeffs(mat_size):
    print("Enter matrix A:")
    matrix_A = np.zeros((mat_size, mat_size))
    for i in range(mat_size):
        for j in range(mat_size):
            matrix_A[i][j] = float(input(f"a[{i}][{j}] = "))

    print("\nEnter vector b:")
    vector_b = np.zeros(mat_size)
    for i in range(mat_size):
        vector_b[i] = float(input(f"b[{i}] = "))


    return matrix_A, vector_b
