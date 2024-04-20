t = int(input())
for _ in range(t):
    changes = 0
    s = input()
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            changes += 1
        l += 1
        r -= 1
    print(changes)