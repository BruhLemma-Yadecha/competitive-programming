n = int(input())
a = list(map(int, input().split()))

hermione = 0
harry = 0

is_hermione = True
# boundaries
i = 0
j = n - 1
while i <= j:
    if is_hermione:
        if a[i] > a[j]:
            hermione += a[i]
            i += 1
        else:
            hermione += a[j]
            j -= 1
    else:
        if a[i] > a[j]:
            harry += a[i]
            i += 1
        else:
            harry += a[j]
            j -= 1
    is_hermione = not is_hermione
print(hermione, harry)