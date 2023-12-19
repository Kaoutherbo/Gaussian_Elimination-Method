
def display_solution(arr_sol, matrix_size):
    print("\nThe solution of this system is:")
    for i in range(matrix_size):
        print(f"X{i+1} = {arr_sol[i]:.2f}", end="\t")
        

def display_eigenvalues_eigenvecors(eigenvalues, eigenvectors):
    print("\nEigenvalue(s):")
    for i, eigenvalue in enumerate(eigenvalues):
        print(f"lambda_{i + 1} = {eigenvalue:.4f}")

    print("\nEigenvector(s):")
    for i, eigenvector in enumerate(eigenvectors.T):
        print(f"v_{i + 1} = [{', '.join(map(lambda x: f'{x:.4f}', eigenvector))}]")
