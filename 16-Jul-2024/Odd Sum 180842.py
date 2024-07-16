# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

n = int(input())
a = list(map(int, input().split()))

# all positive numbers are valid
# subtract the smallest odd number possible from the sum
smallest_odd = float('inf')
sum_ = 0
for i in range(n):
    if a[i] > 0:
        sum_ += a[i]
        if a[i] % 2 != 0:
            smallest_odd = min(smallest_odd, a[i])
    else:
        if a[i] % 2 != 0:
            smallest_odd = min(smallest_odd, abs(a[i]))
            
if sum_ % 2 == 0:
    sum_ -= smallest_odd
print(sum_)