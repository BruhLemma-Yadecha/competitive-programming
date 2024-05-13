n = int(input())
musicians = {}
for _ in range(n):
    x, y = map(int, input().split())
    musicians[y] = musicians.get(y, 0) + x
musicians = [[skill, freq] for skill, freq in musicians.items()]
musicians.sort()
i = 0
j = len(musicians) - 1
res = 0
# pair the musicians with the highest and lowest skill and find the biggest skill sum
while i <= j:
    freq_left = musicians[i][1]
    freq_right = musicians[j][1]
    total_time = musicians[i][0] + musicians[j][0]
    if freq_left == freq_right:
        res = max(res, total_time)
        i += 1
        j -= 1
    elif freq_left < freq_right:
        res = max(res, total_time)
        musicians[j][1] -= freq_left
        i += 1
    else:
        res = max(res, total_time)
        musicians[i][1] -= freq_right
        j -= 1
print(res)
