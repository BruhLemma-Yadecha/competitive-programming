t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [None] * n
    
    a.sort()
    b.sort(reverse=True)
    
