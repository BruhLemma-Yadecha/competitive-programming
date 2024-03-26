from itertools import permutations

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Count the number of elements in a that are greater than or equal to b
    count = sum(1 for i in range(n) if a[i] > b[i])

    # Calculate the number of possible arrangements as the factorial of the count
    num_arrangements = 1
    for i in range(1, count + 1):
        num_arrangements *= i

    print(num_arrangements)
