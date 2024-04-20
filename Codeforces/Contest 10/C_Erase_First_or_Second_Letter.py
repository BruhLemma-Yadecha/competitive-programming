t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    substrings = set()

    for i in range(n):
        substrings.add(s[i:])

    print(len(substrings))
