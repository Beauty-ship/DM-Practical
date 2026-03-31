def compute_degrees(matrix, n):
    print("\nVertex\tIn-Degree\tOut-Degree")
    
    for i in range(n):
        out_degree = sum(matrix[i])  # row sum
        
        in_degree = 0
        for j in range(n):
            in_degree += matrix[j][i]  # column sum
        
        print(f"{i}\t{in_degree}\t\t{out_degree}")


# Input
n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (row-wise):")
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Compute degrees
compute_degrees(matrix, n)