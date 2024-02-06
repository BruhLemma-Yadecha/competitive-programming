if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = []
    for i in arr:
        if i not in l:
            l.append(i)
    l.sort()
    print(l[len(l) - 2])
