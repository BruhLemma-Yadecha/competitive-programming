from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    A = []
    for _ in range(n):
        A.append(list(input()))

    operations = 0
    
    # onion layers of the matrix
    L = []
    j = 0
    for i in range(n // 2):
        l = []
        top = [A[i][x] for x in range(0 + i, n - i)]
        left = [A[x][i] for x in range(0 + i, n - i)]
        bottom = [A[n - 1 - i][x] for x in range(0 + i, n - i)]
        right = [A[x][n - 1 - i] for x in range(0 + i, n - i)]
        left.reverse()
        bottom.reverse()
        
        L.append(top + right + bottom + left)
    for row in L:
        print(''.join(row))
    print()