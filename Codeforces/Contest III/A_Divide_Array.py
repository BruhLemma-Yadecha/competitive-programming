n = int(input())
arr = list(map(int, input().split()))

neg = []
pos = []
zero = []

for i in arr:
    if i > 0:
        pos.append(i)
    elif i < 0:
        neg.append(i)
    else:
        zero.append(i)

if len(neg) % 2 == 0:
    # even size
    if len(neg) == 2:
        zero.append(neg.pop())
    elif len(neg) > 3:
        if len(pos) == 0:
            pos.append(neg.pop())
            pos.append(neg.pop())
            zero.append(neg.pop())
        else:
            zero.append(neg.pop())
if len(pos) == 0 and len(neg) >= 3:
    pos.append(neg.pop())
    pos.append(neg.pop())


print(len(neg), *neg)
print(len(pos), *pos)
print(len(zero), *zero)
