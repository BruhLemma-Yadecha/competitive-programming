n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))

result = -1
i = 0
j = 0
while i < n:
    curr = cities[i]
    while j < m - 1 and (abs(towers[j + 1] - curr) <= abs(towers[j] - curr)):
        j += 1
    result = max(result, abs(towers[j] - curr))
    i += 1
    
print(result)
