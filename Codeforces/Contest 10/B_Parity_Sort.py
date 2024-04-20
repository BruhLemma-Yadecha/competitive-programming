t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    even = [x for x in a if x % 2 == 0]
    odd = [x for x in a if x % 2 == 1]
    even.sort()
    odd.sort()
    i = 0
    j = 0
    res = []
    for val in a:
        if val % 2 == 0:
            res.append(even[i])
            i += 1
        else:
            res.append(odd[j])
            j += 1
    if res == sorted(a):
        print("YES")
    else:
        print("NO")