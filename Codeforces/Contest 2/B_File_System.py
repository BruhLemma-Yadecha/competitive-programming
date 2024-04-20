lines = int(input())
names = {}
for _ in range(lines):
    name = input()
    if name in names:
        print(name + str(names[name]))
        names[name] += 1
    else:
        names[name] = 1
        print('OK')