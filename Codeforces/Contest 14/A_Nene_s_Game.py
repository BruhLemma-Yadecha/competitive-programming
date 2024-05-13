from bisect import bisect_right

t = int(input())
for _ in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    n = list(map(int, input().split()))
    res = []
    for i in n:
        size = i
        while True:
            curr = bisect_right(a, size)
            if curr == 0:
                break
            size -= curr  # remove the dead players
        res.append(size)  # the remaining players
    print(*res)
