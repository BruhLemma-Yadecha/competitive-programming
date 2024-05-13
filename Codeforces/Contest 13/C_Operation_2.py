a, b = map(int, input().split())

# try going the other way???
def min_operations(a, b):
    operations = 0
    while b > a:
        operations += 1
        if b % 2 == 0:
            b //= 2
        else:
            b += 1
    return operations + a - b
print(min_operations(a, b))
