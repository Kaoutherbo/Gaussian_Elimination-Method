from get_coeffs import get_coeffs
from gaussian_elimination import gaussian_elimination
from back_substitution import back_substitution
from display_solution import display_solution
from calculate_determinant import calculate_determinant

def solve_linear_system():
    mat_size = int(input("Enter number of unknowns: "))

    matrix = get_coeffs(mat_size)

    determinant = calculate_determinant(matrix)
    print(f"Determinant of the matrix is: {determinant:.2f}")

    if determinant != 0:
        matrix = gaussian_elimination(matrix, mat_size)

        sol_arr = back_substitution(matrix, mat_size)

        display_solution(sol_arr, mat_size)
    else:
        print("The determinant is zero. The system of equations may have no unique solution.")

if __name__ == "__main__":
    solve_linear_system()
