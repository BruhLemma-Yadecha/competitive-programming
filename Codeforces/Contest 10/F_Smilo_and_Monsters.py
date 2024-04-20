t = int(input())
for _ in range(t):
    hordes = int(input())
    monsters_per_horde = list(map(int, input().split()))
    x = 0
    moves = 0
    for i in range(hordes):
        if monsters_per_horde[i] > x:
            # use move 1 until the number of monsters in the horde is equal to x
            moves += monsters_per_horde[i] - x
            x = monsters_per_horde[i]
        # use move 2
        moves += 1
        x = 0
    print(moves)
