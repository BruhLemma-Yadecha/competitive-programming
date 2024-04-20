n = int(input())
a = list(map(int, input().split()))
a.sort()
res = [None for _ in range(n)]

i, j = 0, n - 1
for k in range(n):
    if k % 2 == 1:
        res[k] = a[j]
        j -= 1
    else:
        res[k] = a[i]
        i += 1
print(*res)