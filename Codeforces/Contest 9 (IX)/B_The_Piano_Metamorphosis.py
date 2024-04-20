n, k = map(int, input().split())
a = list(map(int, input().split()))

# k consecutive elements with the min sum, sliding window
curr_sum = sum(a[:k])
min_sum = curr_sum
min_idx = 0
for i in range(k, n):
    curr_sum += a[i] - a[i - k]
    if curr_sum < min_sum:
        min_sum = curr_sum
        min_idx = i - k + 1
print(min_idx + 1)
