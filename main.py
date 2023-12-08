from get_coeffs import get_coeffs
from  gaussian_elimination import gaussian_elimination
from display_solution import display_solution
from calculate_determinant import calculate_determinant
from print_mat import print_matrix_system
import numpy as np

def solve_linear_system():
    mat_size = int(input("Enter the number of rows of matrix: "))

    matrix_A, vector_B = get_coeffs(mat_size)
    
   # Print the system of linear equations
    print("\nSystem of Linear Equations in matrix form:")
    print_matrix_system(matrix_A, vector_B)
    
    det = calculate_determinant(matrix_A)
    
    if det != 0:
        # Use  Gaussian elimination
        arr_sol = gaussian_elimination(matrix_A, vector_B)

        # Display the solution
        display_solution(arr_sol, mat_size)
    else:
        print("The determinant is zero. The system of equations may have no unique solution.")

if __name__ == "__main__":
    solve_linear_system()
