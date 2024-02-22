board = [input() for _ in range(3)]

ind = set()
pairs = set()

for row in board:
    r = set(row)
    if len(r) == 2:
        # only two players present, so pair winner
        winners = list(r)
        winners.sort() # to make sure no shenanigans happen
        pairs.add((winners[0], winners[1]))
    elif len(r) == 1:
        ind.add(list(r)[0])

columns = [[row[j] for row in board] for j in range(3)]
for row in columns:
    r = set(row)
    if len(r) == 2:
        # only two players present, so pair winner
        winners = list(r)
        winners.sort() # to make sure no shenanigans happen
        pairs.add((winners[0], winners[1]))
    elif len(r) == 1:
        ind.add(list(r)[0])

r = set([board[0][0], board[1][1], board[2][2]])
if len(r) == 2:
    # only two players present, so pair winner
    winners = list(r)
    winners.sort() # to make sure no shenanigans happen
    pairs.add((winners[0], winners[1]))
elif len(r) == 1:
    ind.add(list(r)[0])

r = set([board[0][2], board[1][1], board[2][0]])
if len(r) == 2:
    # only two players present, so pair winner
    winners = list(r)
    winners.sort() # to make sure no shenanigans happen
    pairs.add((winners[0], winners[1]))
elif len(r) == 1:
    ind.add(list(r)[0])


print(len(ind))
print(len(pairs))