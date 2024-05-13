s = input()
n = len(s)
stack = [None] * n
i = 0
j = 0
while i < len(s):
    if s[i] == '<':
        j -= 1
        j = max(j, 0)
        i += 2
    else:
        stack[j] = s[i]
        i += 1
        j += 1
print(*stack[:j], sep="")

# s = input()
# stack = []
# i = 0
# while i < len(s):
#     if s[i] == "<":
#         if stack:
#             stack.pop()
#             i += 2
#     else:
#         stack.append(s[i])
#         i += 1
# print("".join(stack))
