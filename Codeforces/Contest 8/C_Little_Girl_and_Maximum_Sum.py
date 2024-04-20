n, q = map(int, input().split())
a = list(map(int, input().split()))
hits = [0] * n
for _ in range(q):
    l, r = map(int, input().split())
    hits[l - 1] += 1
    if r < n:
        hits[r] -= 1
for i in range(1, n):
    hits[i] += hits[i - 1]
a.sort()
hits.sort()
res = sum([a[i] * hits[i] for i in range(n)])
print(res)
