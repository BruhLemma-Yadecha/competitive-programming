t = int(input())
for _ in range(t):
    res = 0
    n, m = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort(reverse=True)
    
    i = 0
    j = m - 1
    k = n - 1
    
    for _ in range(n):
        t1 = abs(a[k] - b[j])
        t2 = abs(a[i] - b[i])
        if t1 < t2:
            i += 1
        else:
            j -= 1
            k -= 1
            
        res += max(t1, t2)
    
    print(res)
                