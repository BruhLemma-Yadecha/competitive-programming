t = int(input())
for _ in range(t):
    score = 0
    n = int(input())
    lanterns = {}
    for i in range(n):
        tail = list(map(int, input().split()))
        if tail[0] in lanterns:
            lanterns[tail[0]] = max(lanterns[tail[0]], tail[1])
        else:
            lanterns[tail[0]] = tail[1]
    lanterns = sorted([[0, a, b] for a, b in lanterns.items()], key=lambda x:x[0])
    zero = n
    one = 0
    
    while zero > 0:
        # find the next value to use
        cursor = -1
        while cursor >= -len(lanterns) and lanterns[cursor][0] != 0:
            cursor -= 1
        # absorb the score from the top
        score += lanterns[-1][2]
        lanterns[-1][0] = 1 # turned on
        one += 1
        zero -= 1
        while len(lanterns) > 0 and lanterns[-1][1] <= one:
            lanterns.pop()
    print(score)