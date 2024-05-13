n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# try to find a median that can be created within the array
# only the right side matters for median
# For mid to be valid, every number in the second half
# of the array has to be at least equal to it
def valid(median):
    operations = 0
    for i in range(n // 2, n):
        changes = max(median - a[i], 0)
        if changes > k:
            return False
        operations += changes
    return operations <= k  # if not we can't change the array enough for it to work


l = 1
r = 2 * (10**9) + 1
while l < r:
    mid = (l + r + 1) // 2
    locres = valid(mid)
    if valid(mid):
        l = mid
    else:
        r = mid - 1  # since we're maximising
print(l)
