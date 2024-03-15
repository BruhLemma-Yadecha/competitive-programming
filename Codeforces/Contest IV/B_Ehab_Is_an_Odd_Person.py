_ = int(input())
a = list(map(int, input().split()))
hasEven, hasOdd = False, False
for i in a:
    if i % 2 == 0:
        hasEven = True
    else:
        hasOdd = True
    if hasEven and hasOdd:
        break
if hasEven and hasOdd:
    print(*sorted(a))
else:
    print(*a)