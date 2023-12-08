import numpy as np

def print_matrix_system(matrix, vector):
    rows, cols = matrix.shape

    for i in range(rows):
        row_str = "  ".join([f"{matrix[i, j]:<3}" for j in range(cols)])
        if i%2 != 0:
            print(f"| {row_str} | * | X{i} | = {vector[i]:<3}")
        else:
            print(f"| {row_str} |   | X{i} |   {vector[i]:<3}")   
