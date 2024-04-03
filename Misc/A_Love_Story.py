t = int(input())
comp = 'codeforces'
for _ in range(t):
    s = input()
    diff = 0
    for i, j in zip(s, comp):
        if i != j:
            diff += 1
    print(diff)