n, t = map(int, input().split())
a = list(map(int, input().split()))
# looking for the longest block that sums up to t
i, j, loc, res = 0, 0, 0, 0
while i < n:
    # move j until the time is too much
    while j < n and loc + a[j] <= t:
        loc += a[j]
        j += 1
    # compare the subseq
    if loc <= t: # to prevent awkward cases
        res = max(res, j - i)
        loc -= a[i]
        i += 1
print(res)
    