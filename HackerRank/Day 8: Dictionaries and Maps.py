numbers = int(input())
book = {}
for i in range(numbers):
    name, number = input().split()
    book[name] = number
while True:
    try:
        name = input()
        if name in book:
            print(f'{name}={book[name]}')
        else:
            print("Not found")
    except EOFError:
        break
    