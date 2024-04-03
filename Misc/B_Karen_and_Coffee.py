n, k, q = map(int, input().split())

min_temp = float("inf")
max_temp = float("-inf")
temperatures = [0] * 200_003

for _ in range(n):
    l, r = map(int, input().split())
    temperatures[l] += 1
    temperatures[r + 1] -= 1
    min_temp = min(min_temp, l)
    max_temp = max(max_temp, r)

# Calculate cumulative frequencies
for i in range(0, 200_002):
    temperatures[i] += temperatures[i - 1]

for i in range(0, 200_002):
    if temperatures[i] >= k:
        temperatures[i] = 1
    else:
        temperatures[i] = 0
    temperatures[i] += temperatures[i - 1]
    
# Process queries
for _ in range(q):
    l, r = map(int, input().split())
    print(temperatures[r] - temperatures[l - 1])
