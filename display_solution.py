
def display_solution(solution_vector, matrix_size):
    print("\nThe solution of this system is:")
    for i in range(matrix_size):
        print(f"X{i+1} = {solution_vector[i]:.2f}", end="\t")

