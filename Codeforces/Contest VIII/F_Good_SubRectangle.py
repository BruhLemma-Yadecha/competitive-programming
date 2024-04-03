rows, columns = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(rows)]

prefix_sum = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)] # +1 because we need padding
for row in range(rows):
    for col in range(columns):
        prefix_sum[row+1][col+1] = 1 if a[row][col] == 1 else -1
        prefix_sum[row + 1][col + 1] += prefix_sum[row][col + 1] + prefix_sum[row + 1][col] 
        prefix_sum[row + 1][col + 1] -= prefix_sum[row][col]

res = 0 # this is the largest good area

# top left (v, w) to bottom right (x, y)
for i in range(rows):
    for j in range(i, rows):
        height = j - i + 1
        columns_seen = {0: -1} # maps ones to the column they were seen at

        for current_column in range(columns):
            ones = prefix_sum[j + 1][current_column + 1] - prefix_sum[i][current_column + 1]
            if ones in columns_seen:
                # a complement has been seen before so this area is good
                l = (
                    current_column - columns_seen[ones]
                )  # basically the current column and the last column we've seen with this value
                res = max(res, height * l)
            else:
                columns_seen[ones] = current_column
print(res)