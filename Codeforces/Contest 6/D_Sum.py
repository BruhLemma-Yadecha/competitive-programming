def maximize_sum(n, k, a):
    # Handle empty input array
    if not a:
        return 0
    a.sort()

    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            return sum(a)

    # Perform the operations
    while k > 0:
        if a[0] + a[1] <= a[-1]:
            a.pop()
        else:
            a = a[2:]
        k -= 1

    return sum(a)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(maximize_sum(n, k, a))

