from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

l, res = 0, 0
freq = defaultdict(int)
for r in range(n):
    freq[a[r]] += 1
    while freq[a[r]] >= k:
        res += n - r
        freq[a[l]] -= 1
        l += 1
print(res)
