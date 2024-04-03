from math import gcd

n = int(input())

a = list(map(int, input().split()))
suffix_gcd = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suffix_gcd[i] = gcd(suffix_gcd[i + 1], a[i])

prefix_gcd = 0
max_subarray_gcd = 1  # Since all a have at least 1 as GCD

for i in range(n):
    current_subarray_gcd = gcd(prefix_gcd, suffix_gcd[i + 1])
    max_subarray_gcd = max(max_subarray_gcd, current_subarray_gcd)
    prefix_gcd = gcd(prefix_gcd, a[i])

print(max_subarray_gcd)
