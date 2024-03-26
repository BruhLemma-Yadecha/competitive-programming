def twoLargest(arr):
    arr.sort(key=lambda arr: arr[1])
    result = [arr[0]]
    for left, right in arr[1:]:
        if left >= result[-1][1]:
            result.append((left, right))
    result.sort(key=lambda arr: arr[1] - arr[0], reverse=True)
    return result[:2]

def sz(t):
    return t[1] - t[0]

n, S = map(int, input().split())
stones = []
for _ in range(n):
    stones.append(int(input()))
    
# question is basically asking what are the two longest subarrays
# whose elements differ by at most S
# 1 1 2 2 3 3
stones.sort()
i, j = 0, 0
sequences = [] # additions in the form [left, right)
a = (0, 0)
b = (0, 0)
while i < n:
    while j < n and stones[j] - stones[i] <= S:
        j += 1
    sequences.append((i, j))
    if sz((i, j)) > sz(a):
        b = a
        a = (i, j)
    elif sz((i, j)) > sz(b):
        b = (i, j)
    last = stones[i]
    while i < n and stones[i] == last:
        i += 1 # j is now already ahead

print(sz(a) + sz(b))
