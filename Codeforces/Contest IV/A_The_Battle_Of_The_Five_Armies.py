a, b, c, d, e = list(map(int, input().split()))
m, n, o, p, q = list(map(int, input().split()))
first = a*m + b*n + c*o
second = d*p + e*q
if first > second:
    print('WIN')
elif first < second:
    print('LOSE')
else:
    print('DRAW')
