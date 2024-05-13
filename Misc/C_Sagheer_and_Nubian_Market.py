# Faster solution using binary sort
# O(nlogn) to sort a, logn to find k, and O(n) to check if a given k is valid
# so O(nlogn) time and O(n) space
n, S = map(int, input().split())
a = list(map(int, input().split()))
def valid(k):
    loc = sorted([a[i] + (i + 1)*k for i in range(n)]) 
    k_picks = sum(loc[:k])
    return 0 if  k_picks > S else k_picks
l, r = 0, n
while l < r:
    mid = (l + r + 1) // 2
    if valid(mid) > 0:
        l = mid
    else:
        r = mid - 1
print(l, valid(l))
