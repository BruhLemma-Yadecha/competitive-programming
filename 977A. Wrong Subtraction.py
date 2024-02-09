number = input().split()
n = int(number[0])
k = int(number[1])

for i in range(k):
    if n % 10 == 0:
        n //= 10
    else:
        n -= 1
print(n)