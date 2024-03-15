t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    res = 0
    positive = a[0] > 0
    # find the next subseq
    i = 0
    while i < n:
        if positive:
            highest = a[i]
            while i < n and a[i] > 0:
                highest = max(highest, a[i])
                i += 1
        else:
            highest = float("-inf")
            while i < n and a[i] < 0:
                highest = max(highest, a[i])
                i += 1
        # append the highest to res
        res += highest
        positive = not positive
    print(res)
