def all_ones(arr, i, j):
    return arr[i][j] == 1 and arr[i][j + 1] == 1 and arr[i + 1][j] == 1 and arr[i + 1][j + 1] == 1
def set_ones(arr, i, j):
    arr[i][j] = 1
    arr[i][j + 1] = 1
    arr[i + 1][j] = 1
    arr[i + 1][j + 1] = 1

n, m = tuple(map(int, input().split()))
A = []
for i in range(n):
    column = list(map(int, input().split()))
    A.append(column)
B = []
for i in range(n):
    B.append([0 for x in range(m)])

sol = []
# slide across a and check the 2 x 2 around it. If all ones, mirror it
for i in range(n - 1):
    for j in range(m - 1):
        if all_ones(A, i, j):
            set_ones(B, i, j)
            sol.append((i + 1, j + 1))

# final check
valid = True
for a, b in zip(A, B):
    if a != b:
        valid = False
        break

if valid:
    print(len(sol))
    for line in sol:
        print(line[0], line[1])
else:
    print(-1)
