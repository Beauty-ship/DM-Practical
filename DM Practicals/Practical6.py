def is_complete_graph(matrix, n):
    for i in range(n):
        for j in range(n):
            if i == j:
                # No self-loop
                if matrix[i][j] != 0:
                    return False
            else:
                # Every pair must be connected
                if matrix[i][j] != 1:
                    return False
    return True


# Input
n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (row-wise):")
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Check
if is_complete_graph(matrix, n):
    print("The graph is a Complete Graph")
else:
    print("The graph is NOT a Complete Graph")
