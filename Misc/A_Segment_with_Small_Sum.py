n, s = map(int, input().split())
a = list(map(int, input().split()))
i, j, loc, longest = 0, 0, 0, 0

for j in range(n):
    loc += a[j]
    while i <= j and loc > s:
        loc -= a[i]
        i += 1
    longest = max(longest, j - i + 1)

print(longest)