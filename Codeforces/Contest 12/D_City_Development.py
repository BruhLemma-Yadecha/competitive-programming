n = int(input())
height_limit = list(map(int, input().split()))

tallest_configuration = []
tallest_sum = 0

for peak_index in range(n):
    curr = height_limit.copy()
    for i in range(peak_index - 1, -1, -1):
        curr[i] = min(curr[i + 1], curr[i])
    for j in range(peak_index + 1, n):
        curr[j] = min(curr[j - 1], curr[j])
    if (locsum := sum(curr)) > tallest_sum:
        tallest_sum = locsum
        tallest_configuration = curr

print(*tallest_configuration)
