t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    i = 0
    j = n - 1
    while k > 0:
        if a[i] + a[i + 1] <= a[j]:
            i += 2
        else:
            j -= 1
        k -= 1
    print(sum(a[i:j+1]))