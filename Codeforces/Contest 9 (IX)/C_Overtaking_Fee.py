n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

seen = set()
fine = set()
j = 0 # explores b
for i in range(n):
    current_car = a[i]
    if current_car in fine:
        continue
    while True:
        if b[j] == a[i]:
            j += 1
            break
        else:
            fine.add(b[j])
            j += 1
print(len(fine))