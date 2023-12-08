import numpy as np
from back_substitution import back_substitution
from triangularization import triangularization

def  gaussian_elimination(matrix_A, vector_B):
    # Combine matrix A and vector B into an matrix
    matrix = np.column_stack((matrix_A, vector_B))

    # Call the triangularization function
    modified_matrix, modified_vector = triangularization(matrix[:, :-1], matrix[:, -1])

    # Perform back-substitution
    arr_sol = back_substitution(modified_matrix, modified_vector)

    return arr_sol