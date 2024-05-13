t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    # if even b // 2, if odd b // 2 + a
    print(min(n * a, (n // 2) * b + (n % 2) * a))