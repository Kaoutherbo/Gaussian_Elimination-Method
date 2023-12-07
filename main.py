from get_coeffs import get_coeffs
from  gaussian_elimination import gaussian_elimination
from display_solution import display_solution
from calculate_determinant import calculate_determinant

def solve_linear_system():
    mat_size = int(input("Enter number of unknowns: "))

    matrix_A, vector_B = get_coeffs(mat_size)

    det = calculate_determinant(matrix_A)
    print(f"Determinant of the matrix is: {det:.2f}")

    if det != 0:
        # Use  Gaussian elimination
        arr_sol = gaussian_elimination(matrix_A, vector_B)

        # Display the solution
        display_solution(arr_sol, mat_size)
    else:
        print("The determinant is zero. The system of equations may have no unique solution.")

if __name__ == "__main__":
    solve_linear_system()
