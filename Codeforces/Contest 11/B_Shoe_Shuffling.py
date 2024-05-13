t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    res = [i + 1 for i in range(n)]
    ref = {}
    for shoe_size in s:
        ref[shoe_size] = ref.get(shoe_size, 0) + 1
    # if there is a shoe size that belongs to one student only, it is invalid
    invalid = False
    for i in ref.values():
        if i == 1:
            invalid = True
            break
    if not invalid:
        # shuffle each group of shoes by one step
        i = 0
        while i < n:
            j = i + ref[s[i]] - 1
            # skip around
            res[i:j + 1] = [res[j]] + res[i:j]
            i += ref[s[i]]
        print(*res)
    else:
        print(-1)
        continue
         
