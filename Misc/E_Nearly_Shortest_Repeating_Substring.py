t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    for i in range(1, n+1):
        if n % i == 0:
            x = 2
            for j in range(0, i):
                for k in range(j + i, n, i)
                    if s[k] != s[j]:
                        x-=1
            if x > 0:
                print(i)