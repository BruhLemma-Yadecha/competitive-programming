# Problem: B - Remove Smallest - https://codeforces.com/gym/536373/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    valid = True
    for i in range(n - 1):
        diff = abs(a[i] - a[i + 1])
        if diff > 1:
            valid = False
            break
    print('YES' if valid else 'NO')