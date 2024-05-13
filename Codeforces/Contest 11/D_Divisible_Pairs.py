t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    def first_condition(i, j):
        return (a[i] + a[j]) % x == 0

    def second_condition(i, j):
        return (a[i] - a[j]) % y == 0

    ref = {}
    max_elem = -1
    max_idx = -1
    for i in range(n):
        if a[i] > max_elem:
            max_elem = a[i]
            max_idx = i
        if a[i] in ref:
            ref[a[i]].append(i)
        else:
            ref[a[i]] = [i]

        res = 0
    # go through one time, and look for good pairs
    for i in range(n):
        # first condition handling
        comp_base = a[i] % y
        curr = comp_base
        while curr <= max_elem:
            if curr in ref:
                # check every possible index
                for j in ref[curr]:
                    if j >= i and first_condition(i, j):
                        res += 1
            curr += y
    print(res)
