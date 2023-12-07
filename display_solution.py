def display_solution(sol_arr, mat_size):
    print("\nThe solution for this system is:")
    for i in range(mat_size):
        print(f"X{i} = {sol_arr[i]:.2f}", end="\t")
