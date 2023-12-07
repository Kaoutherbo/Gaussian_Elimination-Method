import numpy as np

def calculate_determinant(matrix):
    return np.linalg.det(matrix[:, :-1])
