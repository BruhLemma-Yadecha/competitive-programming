t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    alice = list(input())
    bob = list(input())

    alice.sort()
    bob.sort()

    res = []
    i, j, from_a, from_b = 0, 0, 0, 0

    while i < n and j < m:
        if from_a == k:
            res.append(bob[j])
            j += 1
            from_a = 0
            from_b = 1
            continue
        elif from_b == k:
            res.append(alice[i])
            i += 1
            from_b = 0
            from_a = 1
            continue
        if alice[i] >= bob[j]:
            res.append(bob[j])
            j += 1
            from_b += 1
            from_a = 0
        else:
            res.append(alice[i])
            i += 1
            from_a += 1
            from_b = 0
    print(''.join(res))
