
def display_solution(arr_sol, matrix_size):
    print("\nThe solution of this system is:")
    for i in range(matrix_size):
        print(f"X{i+1} = {arr_sol[i]:.2f}", end="\t")

