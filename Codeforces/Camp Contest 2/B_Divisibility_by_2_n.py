from functools import reduce, cache

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 2 ** n
    prod = reduce(lambda x, y: x * y, a)
    if prod % MOD == 0:
        print(0)
        continue

    @cache
    def count_twos(x):
        res = 0
        while x % 2 == 0:
            res += 1
            x //= 2
        return res

    twos = count_twos(prod)
    to_add_twos = [count_twos(x + 1) for x in range(1, n, 2)]
    av = sum(to_add_twos)

    if twos + av < n:
        print(-1)
        continue

    target = n - twos
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for num in to_add_twos:
        for i in range(target, num - 1, -1):
            dp[i] = min(dp[i], dp[i - num] + 1)

    if dp[target] == float('inf'):
        print(-1)
    else:
        print(dp[target])