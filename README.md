# Gaussian Elimination for Linear Systems

## Overview

This Python project provides functions for solving linear systems of equations using the Gaussian elimination method. The implementation includes functions for obtaining coefficients, calculating determinants, performing Gaussian elimination, back-substitution, and displaying solutions.

## Functions

### 1. `get_coeffs`

Prompt the user to enter the number of unknowns and populate a matrix with coefficients for a linear system.

### 2. `calculate_determinant`

Calculate the determinant of a square matrix using NumPy's `np.linalg.det` function.

### 3. `gaussian_elimination`

Perform Gaussian elimination on an augmented matrix to transform it into upper triangular form.

### 4. `back_substitution`

Solve a linear system in upper triangular form using back-substitution.

### 5. `triangularization`

Combine Gaussian elimination and back-substitution for efficient solution finding.

### 6. `display_solution`

Print the solution vector in a readable format.

### 7. `solve_linear_system`

Main entry point: obtain coefficients, calculate determinant, and solve the linear system using Gaussian elimination.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Kaoutherbo/Gaussian_Elimination-Method.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Gaussian-Elimination-Method
    ```

3. Run the main script:

    ```bash
    python main.py
    ```

Follow the on-screen instructions to input coefficients and obtain solutions.

## Dependencies

- NumPy: [Installation instructions](https://numpy.org/install/)

## Contributing

If you would like to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
