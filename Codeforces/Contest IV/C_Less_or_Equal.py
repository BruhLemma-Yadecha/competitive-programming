n, k = tuple(map(int,input().split()))
a = list(map(int,input().split()))
a.sort()
# the first k elements of a are the target, so try getting a number one above that
if a[k] < 0:
    print(1)
else:
    res = a[k] + 1
    if res > 1_000_000_000:
        print(-1)
    else:
        print(res)