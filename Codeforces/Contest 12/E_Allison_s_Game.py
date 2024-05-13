from math import sqrt

n = int(input())
h = list(map(int, input().split()))


class Entry:
    def __init__(self, position, height):
        self.position = position
        self.height = height


h = [Entry(p, H) for p, H in enumerate(h)]

i = 0
res = 0
stack = []  # monotonically decreasing stack
left = -1

def consider(entry):
    global res
    width = i if not stack else i - stack[-1].position - 1
    side = min(width, entry.height)
    res = max(res, side**2)

while i < n:
    while stack and h[i].height < stack[-1].height:
        consider(stack.pop())
    stack.append(h[i])
    i += 1

# if there is anything left at the end, clean it out
while stack:
    consider(stack.pop())
print(int(sqrt(res)))

# # using a min monotonic stack and checking whenever we find a bigger element
# # than the one at the top
# i = 0
# stack = []
# res = 0
# while i < n:
#     while stack and h[i].height > stack[-1].height:
#         top_of_stack = stack.pop()
#         width = i if not stack else i - stack[-1][1] - 1
#         res = max(res, top_of_stack[0] * width)
#     stack.append((h[i], i))
#     i += 1

# # Handle remaining bars in the stack
# while stack:
#     top_of_stack = stack.pop()
#     width = n if not stack else n - stack[-1][1] - 1  # Correctly calculate the width
#     res = max(res, top_of_stack[0] * width)

# print(res)
