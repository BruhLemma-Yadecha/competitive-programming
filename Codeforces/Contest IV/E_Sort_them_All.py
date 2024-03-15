t = int(input())
for _ in range(t):
    n = int(input())
    a = [(k, v) for v, k in enumerate(list(map(int, input().split())))]
    b = list(map(int, input().split()))

    moves = []
    # selection sort the array in a
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]
                moves.append((j+2, j+1))

    # crawl through b and see if it is sorted
    ref = [v for _, v in a]
    b = [b[i] for i in ref]
    if len(moves) <= 10_000 and all(b[i] <= b[i + 1] for i in range(n - 1)):
        print(len(moves))
        for move in moves:
            print(*move)
    else:
        print(-1)