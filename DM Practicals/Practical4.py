def generate_solutions(n, C):
    solution = [0] * n

    def brute_force(index, remaining):
        # If we reached last variable
        if index == n - 1:
            solution[index] = remaining
            print(solution)
            return
        
        # Try all possible values for current variable
        for i in range(remaining + 1):
            solution[index] = i
            brute_force(index + 1, remaining - i)

    brute_force(0, C)


# Input
n = int(input("Enter value of n: "))
C = int(input("Enter value of C (<=10): "))

print("\nSolutions:")
generate_solutions(n, C)