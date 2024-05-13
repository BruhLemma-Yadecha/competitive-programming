t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        hashes = False
        if i % 2 == 0:
            hashes = True
        row = ['.'] * (2 * n)
        j = 0
        while j < 2 * n - 1:
            if hashes:
                row[j] = '#'
                row[j + 1] = '#'
            hashes = not hashes
            j += 2
        print(*row,sep="")
        print(*row,sep="")
                