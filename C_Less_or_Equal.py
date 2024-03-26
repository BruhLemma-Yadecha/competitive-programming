def lessOrEqual(n, k, a) -> None:
    a.sort()
    res = None
    if k == 0: # the pick has to be entirely outside the list
        if a[0] == 1:
            print(-1)
            return
        res = a[0] - 1
    else: # pick the last element of the first k elements.
        res = a[k - 1] # -1 because less OR EQUAL, not just less
    # check if the pick works
    i = 0
    while i < n and a[i] <= res:
        i += 1
    if i != k:
        print(-1)
    else:
        print(res)

n, k = map(int, input().split())
a = list(map(int, input().split()))
lessOrEqual(n, k, a)