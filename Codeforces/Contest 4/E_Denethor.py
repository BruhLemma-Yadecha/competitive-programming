t = int(input())
for _ in range(t):
    n = int(input())
    first = list(map(int, input().split()))
    last = list(map(int, input().split()))
    # look for the first occurrence of the first index in last
    idx = 0
    while idx < n and first[idx] == last[idx]:
        idx += 1
    if idx == n:
        print(0) # no deployments happened
    else:
        print(last.index(first[idx]))
