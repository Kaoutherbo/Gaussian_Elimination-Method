from get_coeffs import get_coeffs
from  gaussian_elimination import gaussian_elimination
from display_solution import display_solution
from calculate_determinant import calculate_determinant
from print_mat import print_matrix_system
from calculate_eigenvalues_eigenvectors import calculate_eigenpairs
from display_solution import display_eigenvalues_eigenvecors

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
        
        # Calculate and display eigenvalues and eigenvectors
        eigenvalues, eigenvectors = calculate_eigenpairs(matrix_A)
        # print("\nEigenvalues of this matrix are:", eigenvalues)
        # print("\nEigenvectors of this matrix are:", eigenvectors)
        display_eigenvalues_eigenvecors(eigenvalues, eigenvectors)
    
    else:
        print("The determinant is zero. The system of equations may have no unique solution.")

if __name__ == "__main__":
    solve_linear_system()
