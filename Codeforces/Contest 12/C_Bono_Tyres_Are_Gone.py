n = int(input())
pile = []
next_tyre = 1
shufflings = 0
for _ in range(2 * n):
    command = list(input().split())
    if len(command) == 2:
        tyre = int(command[1])
        pile.append(tyre)
    else:
        if pile:
            if next_tyre != pile[-1]:
                shufflings += 1
                pile = []
            else:
                pile.pop()
        next_tyre += 1
print(shufflings)
