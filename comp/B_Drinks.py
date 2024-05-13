drinks = int(input())
percentages = input().split()
total = 0
for p in percentages:
    total += float(p)
total /= drinks 
print(total)