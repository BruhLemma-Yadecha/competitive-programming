t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    i, j, res = 0, 0, 0
    while j < n:
        if a[j] >= j - i + 1:
            res += j - i + 1
            j += 1
        else:
            i += 1
    print(res)