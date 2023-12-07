# Linear System Solver

## Overview

This Python program solves a system of linear equations using the Gaussian elimination method. The program is organized into modular functions, each serving a specific purpose.

## Functions

### 1. `input_functions.py`

This module contains the function for inputting coefficients of the linear system.

```python
def input_coefficients(matrix_size):
    """
    Accepts user input for the coefficients of a linear system.

    Parameters:
    - matrix_size (int): Number of unknowns in the system.

    Returns:
    - matrix_input (numpy.ndarray): Coefficient matrix augmented with the right-hand side.
    """
    # Implementation details...
2. gaussian_elimination.py
This module performs Gaussian elimination on the coefficient matrix.

python
Copy code
def gaussian_elimination(matrix_input, matrix_size):
    """
    Applies Gaussian elimination to the coefficient matrix.

    Parameters:
    - matrix_input (numpy.ndarray): Coefficient matrix augmented with the right-hand side.
    - matrix_size (int): Number of unknowns in the system.

    Returns:
    - matrix_input (numpy.ndarray): Triangularized coefficient matrix.
    """
    # Implementation details...
3. back_substitution.py
This module performs back substitution to find the solution vector.

python
Copy code
def back_substitution(matrix_input, matrix_size):
    """
    Performs back substitution to find the solution vector.

    Parameters:
    - matrix_input (numpy.ndarray): Triangularized coefficient matrix.
    - matrix_size (int): Number of unknowns in the system.

    Returns:
    - solution_vector (numpy.ndarray): Solution vector for the linear system.
    """
    # Implementation details...
4. display_functions.py
This module contains a function to display the solution vector.

python
Copy code
def display_solution(solution_vector, matrix_size):
    """
    Displays the solution vector in a readable format.

    Parameters:
    - solution_vector (numpy.ndarray): Solution vector for the linear system.
    - matrix_size (int): Number of unknowns in the system.

    Returns:
    - None
    """
    # Implementation details...
5. determinant_function.py
This module calculates the determinant of the coefficient matrix.

python
Copy code
def calculate_determinant(matrix_input):
    """
    Calculates the determinant of the coefficient matrix.

    Parameters:
    - matrix_input (numpy.ndarray): Coefficient matrix augmented with the right-hand side.

    Returns:
    - determinant (float): Determinant of the coefficient matrix.
    """
    # Implementation details...
6. main_program.py
The main program that orchestrates the functions.

python
Copy code
def solve_linear_system():
    """
    Solves a system of linear equations using Gaussian elimination.

    Parameters:
    - None

    Returns:
    - None
    """
    # Implementation details...
Usage
To use this program, run main_program.py. Follow the prompts to input coefficients and obtain the solution.

License
This project is licensed under the MIT License - see the LICENSE file for details.




