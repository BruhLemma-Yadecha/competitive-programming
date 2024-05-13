t = int(input())
x = 0
stack = [1]
MAX = 2**32
for _ in range(t):
    inp = list(input().split())
    command = inp[0]
    if command == "add":
        x += stack[-1]
        if x >= MAX:
            print("OVERFLOW!!!")
            exit()
    elif command == "for":
        loops = int(inp[1])
        value = stack[-1] if stack[-1] < MAX else MAX # to prevent funny business
        stack.append(value * loops)
    else:
        stack.pop()
print(x)