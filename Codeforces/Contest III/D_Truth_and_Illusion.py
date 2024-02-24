from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    A = []
    for _ in range(n):
        A.append(list(input()))
    
    operations = 0
    
    # Check and adjust diagonal elements
    for i in range(n):
        if A[i][i] != A[n-1-i][n-1-i]:
            operations += 1
            A[i][i] = A[n-1-i][n-1-i]
    
    # Adjust upper triangular part to match lower triangular part
    for i in range(n):
        for j in range(i + 1, n):
            if A[i][j] != A[j][i]:
                operations += 1
                A[i][j] = A[j][i]
    
    print(operations)
