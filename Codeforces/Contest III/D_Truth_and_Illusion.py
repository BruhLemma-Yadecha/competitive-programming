from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    A = []
    for _ in range(n):
        A.append(list(input()))

    operations = 0
    
    # generate the four triangles
    top = []
    left = []
    for i in range(n // 2):
        T = [A[i][x] for x in range(0 + i, n - i)]
        L = [A[x][i] for x in range(0 + i, n - i)]
        for val in T:
            top.append(val)
        for val in L:
            left.append(val)

    if n % 2 == 1:
        top.append(A[n // 2][n // 2])
        left.append(A[n // 2][n // 2])
    
    bottom = []
    right = []
    j = 0
    for i in range(n - 1, n // 2 - 1, -1):
        B = [A[i][x] for x in range(0 + j, n - j)]
        R = [A[x][i] for x in range(0 + j, n - j)]
        for val in B:
            bottom.insert(0, val)
        for val in R:
            right.insert(0, val)
        j += 1
        
    
    # which triangle to enforce
    top_one = top.count('1')
    bottom_one = bottom.count('1')
    left_one = left.count('1')
    right_one = right.count('1')

    top_changes = abs(top_one - bottom_one) + abs(top_one - left_one) + abs(top_one - right_one)
    bottom_changes = abs(bottom_one - top_one) + abs(bottom_one - left_one) + abs(bottom_one - right_one)
    right_changes = abs(right_one - top_one) + abs(right_one - bottom_one) +abs(right_one - left_one)
    left_changes = abs(left_one - top_one) + abs(left_one - bottom_one) + abs(left_one - right_one)
    
    print(min(top_changes, bottom_changes, left_changes, right_changes))
