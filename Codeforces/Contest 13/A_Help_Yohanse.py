n = int(input())
# print an array that is one step away from being done
arr = [n] + list(range(1, n))
print(*arr)