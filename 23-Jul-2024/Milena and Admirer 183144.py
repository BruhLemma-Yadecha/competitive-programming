# Problem: Milena and Admirer - https://codeforces.com/problemset/problem/1898/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
        
    res = 0
    global_maximum = a[-1]
    i = n - 2
    while i >= 0:
        if a[i] > global_maximum:
            # needs to be split into smaller parts
            parts = (a[i] + global_maximum - 1) // global_maximum
            res += parts - 1
            global_maximum = a[i] // parts
        else:
            global_maximum = a[i]
        i -= 1

    print(res)