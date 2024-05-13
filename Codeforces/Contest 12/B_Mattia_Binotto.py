n=int(input())
t=list(map(int, input().split()))
t.sort() # the drivers at the beginning of the array likely don't have an issue
time = 0
satisfied = 0
for pit in t:
    if pit >= time:
        satisfied += 1
        time += pit
    # if they wouldn't be satisfied at the earliest possible opening, ignore them
print(satisfied)


