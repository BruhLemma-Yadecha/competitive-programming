n = int(input())
arr = list(map(int, input().split()))

# target
    # a, b, and c have at least one element

a = [x for x in arr if x < 0]
b = [x for x in arr if x > 0]
c = [x for x in arr if x == 0]

if len(a) % 2 == 0:
    if len(b) == 0:
        if len(a) >= 2:
            b.append(a.pop())
            b.append(a.pop())
        else:
            b.append(a.pop())
            c.append(a.pop())
    else:
        c.append(a.pop())

if len(b) == 0 and len(a) % 2 == 1:
    if len(a) >= 2:
        b.append(a.pop())
        b.append(a.pop())

print(len(a), end=' ')
print(*a)
print(len(b), end=' ')
print(*b)
print(len(c), end=' ')
print(*c)
