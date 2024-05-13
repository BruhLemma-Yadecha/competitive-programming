a, m = map(int, input().split())
twos = a // 2
a -= twos * 2
ones = a
a = 0
while (ones + twos) % m != 0 and twos > 0:
    twos -= 1
    ones += 2
if (ones + twos) % m == 0:
    print(ones + twos)
else:
    print(-1)
