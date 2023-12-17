import numpy as np

def power_iteration(matrix_A, tolerance=1e-8, max_iterations=1000):
    n = len(matrix_A)
    vector_initial = np.random.rand(n)
    lambda_prev = 0

    for _ in range(1, max_iterations + 1):
        vector_propre_estime = matrix_A @ vector_initial
        lambda_estime = np.dot(vector_initial, vector_propre_estime)
        vector_initial = vector_propre_estime / np.linalg.norm(vector_propre_estime)

        if np.abs(lambda_estime - lambda_prev) < tolerance:
            return lambda_estime, vector_initial

        lambda_prev = lambda_estime

    return lambda_estime, vector_initial

def calculate_eigenpairs(matrix_A, num_eigenvalues=None):
    eigenvalues = []
    eigenvectors = []
    num_eigenvalues = num_eigenvalues or len(matrix_A)

    for _ in range(num_eigenvalues):
        eigenvalue, eigenvector = power_iteration(matrix_A)
        matrix_A = matrix_A.astype(float) - eigenvalue * np.outer(eigenvector, eigenvector)
        eigenvalues.append(eigenvalue)
        eigenvectors.append(eigenvector)

    return np.array(eigenvalues), np.array(eigenvectors)

