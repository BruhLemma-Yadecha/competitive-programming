n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

i = 0
j = 0
started = 0
sum_a = 0
sum_b = 0

while i < n or j < m:
    # Increment sum_a and sum_b only if there are elements left in their respective lists
    if i < n:
        sum_a += a[i]
        i += 1
    if j < m:
        sum_b += b[j]
        j += 1

    # If the sums are equal, increment started and reset sums
    if sum_a == sum_b:
        started += 1
        sum_a = 0
        sum_b = 0
    # If the sums are not equal and we have exhausted elements in one of the lists, break
    elif (i == n and sum_a != sum_b) or (j == m and sum_a != sum_b):
        started = -1
        break

print(started)
