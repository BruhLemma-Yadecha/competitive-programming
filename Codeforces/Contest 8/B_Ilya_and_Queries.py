s = input()
n = len(s)
consecutive = [0] * n
for i in range(1, n):
    if s[i] == s[i - 1]:
        consecutive[i] = consecutive[i - 1] + 1
    else:
        consecutive[i] = consecutive[i - 1]
# query section
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    res = consecutive[r - 1] - consecutive[l - 1]
    print(res)
        