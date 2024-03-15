t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = 1001
    for i in range(1, n):
        gap = abs(arr[i] - arr[i - 1])
        res = min(res, gap)
    print(res)