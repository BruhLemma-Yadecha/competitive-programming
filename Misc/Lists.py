if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        command = input().split()
        operation = command[0]
        if operation == 'append':
            l.append(int(command[1]))
        elif operation == 'insert':
            l.insert(int(command[1]), int(command[2]))
        elif operation == 'print':
            print(l)
        elif operation == 'remove':
            l.remove(int(command[1]))
        elif operation == 'sort':
            l.sort()
        elif operation == 'pop':
            l.pop()
        elif operation == 'reverse':
            l.reverse()
