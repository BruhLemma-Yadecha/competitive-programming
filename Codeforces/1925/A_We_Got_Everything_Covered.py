t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    letters = 'abcdefghijklmnopqrstuvwxyz'
    print(letters[:k] * n)