from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    log = input()
    res = 0
    freq = Counter(log)
    for key in freq:
        if freq[key] >= ord(key) - ord('A') + 1:
            res += 1
    print(res)