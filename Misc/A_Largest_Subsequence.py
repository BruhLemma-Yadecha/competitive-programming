t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    sorted_s = sorted(s)
    if sorted_s == s:
        print(0)
        continue
    stack = []
    alt = []
    # monotonic stack???
    for i in range(n):
        while stack and s[i] > stack[-1]:
            stack.pop()
            alt.pop()
        stack.append(s[i])
        alt.append(i)
    stack.reverse() # doing the right shift for each subset
    for i in range(len(stack)):
        s[alt[i]] = stack[i]
    if s == sorted_s:
        # count the duplicates at the end
        i = len(stack) - 1
        while i >= 0 and stack[i] == stack[i -]
        duplicates = len(stack) - i
        print(len(alt) - duplicates)
    else:
        print(-1)  