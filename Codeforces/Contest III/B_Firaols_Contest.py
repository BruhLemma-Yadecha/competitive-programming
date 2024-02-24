n, m = tuple(map(int, input().split()))
problems = list(map(int, input().split()))
state = []
found = {i:0 for i in range(1, n + 1)}
unique = 0
hold = True
for i in problems:
    if i not in found:
        found[i] = 1
        unique += 1
    else:
        if found[i] == 0:
            found[i] = 1
            unique += 1
        else:
            found[i] += 1
    if unique >= n:
        good = 0
        for i in range(1, n + 1):
            if found[i] >= 1:
                good += 1
        if good == n:
            state.append('1')
            for i in range(1, n + 1):
                found[i] -= 1
                if found[i] == 0:
                    unique -= 1
    else:
        state.append('0')

print(''.join(state))