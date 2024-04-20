n = int(input())
arr = list(map(int, input().split()))
swaps = []
# using selection sort
for i in range(n):
    cursor = i
    for j in range(i + 1, n):
        if arr[j] < arr[cursor]:
            cursor = j
    if cursor != i:
        arr[i], arr[cursor] = arr[cursor], arr[i]
        swaps.append((i, cursor))
print(len(swaps))
for j in swaps:
    print(j[0], j[1])