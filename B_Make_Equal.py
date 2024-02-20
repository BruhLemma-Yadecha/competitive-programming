def realloc(a, n):
    target = sum(a) // n
    for i in range(n - 1):
        if a[i] > target:
            # take the excess and put it in the next element
            a[i + 1] += a[i] - target
            a[i] = target
        elif a[i] < target:
            return False
    return a[-1] == target
            

cases = int(input())
for _ in range(cases):
    n = int(input())
    a = list(map(int, input().split()))
    if realloc(a, n):
        print("YES")
    else:
        print("NO")