cases = int(input())
results = []
for i in range(cases):
    case = input().split()
    n = int(case[0])
    x1 = int(case[1])
    y1 = int(case[2])
    x2 = int(case[3])
    y2 = int(case[4])

    right_row = [x for x in range(0, 8)]
    right_column = [x for x in range(0, n/2)]
    left_row = [x for x in range()]

    energy = 0
    while x1 != x2 and y1 != y2:
        # when x is 1, you can move from 1 to 8
        # when x is 2, you can move from 2 to 7
        # x is 3 from
        x_movement = [x for x in range(x1, n - x1 + 1)]
        y_movement = [x for x in range(y1, n - y1 + 1)]
        if x2 not in x_movement:
            while x2 != x1:
            if x2 > x1:
                x1 += 1
            elif x2 < x1:
                x1 -= 1
            x_movement = [x for x in range(x1, n - x1 + 1)]
            # spend energy to move there
            
    results.append(energy)
for result in results:
    print(result)