from collections import Counter

n, k = tuple(map(int, input().split()))
a = list(map(int, input().split()))
a = Counter(a)
a = sorted([(k,v) for k,v in a.items()], key=lambda x:x[0])

# Try to get k values from a
last = a[0][0]
so_far = 0
i = 0
valid = True

while i < len(a) and so_far < k:
    if so_far + a[i][1] > k:
        valid = False
        break
    else:
        last = a[i][0]
        so_far += a[i][1]
        i += 1

if k != 0 and valid and 1 <= last + 1 <= 1_000_000_000:
    print(last + 1)
else:
    print(-1)
