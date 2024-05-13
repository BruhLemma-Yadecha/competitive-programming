cases = int(input())
results = []
for i in range(cases):
    n = int(input())
    beauties = list(map(int, input().split()))
    # find three most beautiful
    a = 0
    a_index = -1
    b = 0
    b_index = -1
    c = 0
    c_index = -1
    for index, i in enumerate(beauties):
        if i > a:
            a = i
            a_index = index
            continue
        elif i > b:
            b = i
            b_index = index
            continue
        elif i > c:
            c = i
            c_index = index
            continue
    print(f'{a}, {b}, {c}')

    # check every starting position and every possible combo that is at least 3 stands long
    max_beauty = 0
    for l in range(0, n - 2):
        for r in range(l + 2, n):
            sequence = list(range(l, r + 1))
            # check if the sequence includes the three top spots
            if (a_index not in sequence) or (b_index not in sequence) or (c_index not in sequence):
                continue
            local_sum = 0
            for i in sequence:
                local_sum += beauties[i]
            local_sum -= (r - l)
            if local_sum > max_beauty:
                max_beauty = local_sum
        
    results.append(max_beauty)
for i in results:
    print(i)
    