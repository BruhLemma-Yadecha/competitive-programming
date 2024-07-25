# Problem: E - World is Mine - https://codeforces.com/gym/536373/problem/E

from heapq import heappop, heappush
from collections import Counter


def solve():
    _ = int(input())
    nums = list(map(int, input().split()))

    freq = sorted([[key, value] for key, value in Counter(nums).items()])

    rem_round, removed = 1, 0
    max_heap = []

    for i in range(1, len(freq)):
        if freq[i][1] > rem_round:
            if max_heap and -max_heap[0] > freq[i][1]:
                rem_round -= heappop(max_heap) + freq[i][1]
                heappush(max_heap, -freq[i][1])
            
            rem_round += 1

        else:
            removed += 1
            rem_round -= freq[i][1]
            heappush(max_heap, -freq[i][1])

    print(len(freq) - removed)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
