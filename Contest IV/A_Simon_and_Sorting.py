t = int(input())
for _ in range(t):
    s = input();
    final = sorted(s)
    swap_request = None
    valid = True
    for index, val in enumerate(s):
        dist = abs(final.index(val) - index)
        if dist != 0:
            if swap_request == None:
                swap_request = dist
            else:
                if swap_request != dist:
                    valid = False
                break
                
    if valid:
        print('YES')
    else:
        print('NO')