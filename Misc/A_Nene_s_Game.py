from bisect import bisect_right

R = lambda: map(int, input().split())
t = int(input())

for _ in range(t):
    k, q = R()
    hit_list = list(R())
    q = list(R())
    res = []

    # Calculate the prefix sum array
    prefix_sum = [0] * (k + 1)
    for i in range(1, k + 1):
        prefix_sum[i] = prefix_sum[i - 1] + hit_list[i - 1]

    for player_count in q:
        # Use binary search to find the largest number of hits that is less than or equal to the player count
        idx = bisect_right(prefix_sum, player_count)
        if idx > 0 and prefix_sum[idx - 1] == player_count:
            idx -= 1
        res.append(player_count - prefix_sum[idx])

    print(*res)
