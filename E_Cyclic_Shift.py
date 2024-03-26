n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(input().split()))
print(a)
b = []
invalid = False
for row in range(n):
    r = [-1 for _ in range(m)]
    for column in range(m):
        i = 0
        j = m - 1
        # find the distance to the nearest 1
        while i <= j:
            if i >= j:
                invalid = True
                break
            elif a[row][i] == "1":
                r[column] = i
            elif a[row][j] == "1":
                r[column] = j - (m - 2)
            i += 1
            j -= 1
    b.append(r)
    if invalid:
        break
print(*b)