n, k = map(int, input().split())
a = list(map(int, input().split()))

# smoothing out the array as much as possible
# decreasing may be a bit of an issue
a.sort()
print(*a)

# process possible values with a[-1] as the anchor

res = float('inf')

# find the rightmost element smaller than x using binary search, call it R
def find_rightmost_smaller(x):
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    return l - 1

def operations_to_make_equal(x, l, r):
    res = 0
    for i in range(l, r + 1):
        res += abs(a[i] - x)
    return res

# for i in range(1-k, a[-1] + 1):
#     rmsmlst = find_rightmost_smaller(i)
#     print(i, a[:rmsmlst + 1], operations_to_make_equal(i, 0, rmsmlst))
    
l = 1 - k
r = a[-1]
# find the largest number that still obeys operations <= k using binary search
while l < r:
    m = (l + r + 1) // 2
    rmsmlst = find_rightmost_smaller(m)
    op = operations_to_make_equal(m, 0, rmsmlst)
    print(m, a[:rmsmlst + 1], op)
    if op <= k:
        res = min(res, operations_to_make_equal(m, 0, rmsmlst))
        l = m
    else:
        r = m - 1
print(l)

def find_leftmost_larger(x):
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
    if a[m] > x:
        r = m - 1
    else:
        l = m
    return r

for i in range(n):
    loc = find_leftmost_larger(a[i])
    print(a[i], a[loc:])

# process possible values with a[0] as the anchor
l = a[0]
r = 10**15

# find
