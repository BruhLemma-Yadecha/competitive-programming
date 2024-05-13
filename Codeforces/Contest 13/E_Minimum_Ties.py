t = int(input())

MATCH_LOSS = 0
MATCH_WIN = 3
MATCH_TIE = 1
MATCH_INVALID = 2


def count_outcomes(matches):
    wins = matches.count(MATCH_WIN)
    losses = matches.count(MATCH_LOSS)
    free = len(matches) - wins - losses - 1
    return wins, losses, free


def print_custom_order(fixtures):
    for i in range(n):
        for j in range(i + 1, n):
            res = 0
            if fixtures[i][j] == MATCH_WIN:
                res = 1
            elif fixtures[i][j] == MATCH_LOSS:
                res = -1
            print(res, end="")
            if j != n - 1:
                print(" ", end="")
        if i != n - 1:
            print(" ", end="")

# 0 - loss, 3 - win, 1 - tie, 2 - invalid
for _ in range(t):
    n = int(input())
    if n == 2:
        print(0)  # only one match, so has to be one tie.
        continue

    fixtures = [[2 for _ in range(n)] for _ in range(n)]
    def reflect_row(row):
        for j in range(n):
            if fixtures[row][j] == 0:
                fixtures[j][row] = 3
            elif fixtures[row][j] == 3:
                fixtures[j][row] = 0
            elif fixtures[row][j] == 1:
                fixtures[j][row] = 1

    # first row custom settings
    for i in range(1, n // 2 + 1):
        fixtures[0][i] = 3
    for i in range(n // 2 + 1, n):
        fixtures[0][i] = 0
    if n % 2 == 0:
        fixtures[0][n // 2] = 1
    reflect_row(0)
    
    # generate the rest of the fixtures
    for row in range(1, n):
        wins, losses, free = count_outcomes(fixtures[row])
        
        # add wins into free slots until you have n // 2 wins
        for i in range(n):
            if i != row and fixtures[row][i] == 2 and wins < n // 2:
                fixtures[row][i] = 3
                wins += 1
        # add losses into free slots until you have n // 2 losses
        for i in range(n):
            if i != row and fixtures[row][i] == 2 and losses < n // 2:
                fixtures[row][i] = 0
                losses += 1
        # add a tie if we have an odd number of fixtures
        if n % 2 == 0 and n // 2 + row < n:
            fixtures[row][n // 2 + row] = 1
        reflect_row(row)
            

    print_custom_order(fixtures)
# print the custom order
# for i in range(1, n + 1):
#     for j in range(i + 1, n + 1):
#         if (i, j) in matches:
#             print(matches[(i, j)], end="")
#         elif (j, i) in matches:
#             print(-matches[(j, i)], end="")  # reverse the result
#         if j != n:
#             print(" ", end="")
#     if i != n - 1:
#         print(" ", end="")

# # debug order
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j != i:
#             if (i, j) in matches:
#                 print(i, j, matches[(i, j)])
#             elif (j, i) in matches:
#                 print(i, j, -matches[(j, i)])  # reverse the result
#     print()
# def print_fixtures(fixtures):
#     for team_fixtures in fixtures:
#         print(*team_fixtures)
#     print()

# def print_team_order(fixtures):
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 if fixtures[i][j] == 3:
#                     print(i + 1, j + 1, "W")
#                 elif fixtures[i][j] == 0:
#                     print(i + 1, j + 1, "L")
#                 else:
#                     print(i + 1, j + 1, "D")
#         print()
