from collections import Counter

N = int(input())
a = Counter(map(int, input().split()))
b = Counter(map(int, input().split()))
c = Counter(map(int, input().split()))

x = {}
for i in range(N):
    if 

pairs = 0
for i in a:
    if i in x:
        pairs += a[i] * x[i]
print(pairs)