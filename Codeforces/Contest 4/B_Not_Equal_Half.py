_ = int(input())
a = list(map(int, input().split()))
if len(set(a)) == 1:
    print(-1) # all elements equal
else:
    print(*sorted(a))