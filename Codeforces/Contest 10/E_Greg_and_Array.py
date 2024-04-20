n, m, k = map(int, input().split())
a = list(map(int, input().split()))
pre = [0] * (n + 2)
operations = [None] * m
for i in range(m):
    l, r, d = map(int, input().split())
    operations[i] = (l, r, d)

ops = [0] * (m + 1)
for _ in range(k):
    x, y = map(int, input().split())
    ops[x - 1] += 1
    ops[y] -= 1

times = 0
for i in range(m):
    times += ops[i]
    l, r, d = operations[i]
    pre[l] += times * d
    pre[r + 1] -= times * d

for i in range(1, n + 1):
    pre[i] += pre[i - 1]

for i in range(n):
    a[i] += pre[i + 1]

print(*a)
