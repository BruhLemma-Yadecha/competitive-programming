cases = int(input())
result = []
for i in range(cases):
    constraint_count = int(input())
    bottom = 0
    top = 10_000_000_000
    blacklist = set()

    for j in range(constraint_count):
        constraint = input().split()
        value = int(constraint[1])

        if constraint[0] == '1':
            bottom = max(bottom, value)
        elif constraint[0] == '2':
            top = min(top, value)
        else:
            blacklist.add(value)
    possible_values = list(range(bottom, top + 1))
    blacklist = [x for x in blacklist if x in possible_values]
    result.append(len(possible_values) - len(blacklist))
for i in result:
    print(i)