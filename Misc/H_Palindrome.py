t = int(input())
for _ in range(t):
    s = input()
    if s == s[::-1]:
        print("YES")
    else:
        print("NO")