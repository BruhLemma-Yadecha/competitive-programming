cases = int(input())
results = []
for i in range(cases):
    size = int(input())
    arr = input().split()
    freq = {}
    for c in arr:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    target = -1
    for number, frequency in freq.items():
        if frequency >= 3:
            target = number
            break
    results.append(target)
for i in results:
    print(i)