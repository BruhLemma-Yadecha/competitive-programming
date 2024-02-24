t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    f = input()

    s_count = s.count('1')
    f_count = f.count('1')

    add = retire = move = 0
    if s_count > f_count:
        retire = s_count - f_count
    elif f_count > s_count:
        add = f_count - s_count
    print(max(add, retire))
