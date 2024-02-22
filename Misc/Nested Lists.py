if __name__ == '__main__':
    l = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append((name, score))
        if score not in scores:
            scores.append(score)
    scores.sort()
    second_highest = scores[1]
    names = []
    for name, score in l:
        if score == second_highest:
            names.append(name)
    names.sort()
    for name in names:
        print(name)
 