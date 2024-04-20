t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())

    operations = 0
    A = [idx for idx, val in enumerate(s) if val == 'A']
    valid = [True for _ in range(n)]
    for i in range(len(A) - 1, -1, -1):
        # move it up the chain until it enters an invalid position
        j = A[i]
        while True:
            if j + 1 >= n:
                break # reached the edge
            if s[j + 1] == 'B' and valid[j]:
                # do a swap
                s[j], s[j + 1] = s[j + 1], s[j]
                valid[j] = False
                operations += 1
                j += 1
            else:
                break
    print(operations)
    
            
