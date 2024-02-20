def find(a, target):
    n = len(a)
    # just do pairs
    pairs = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                sum = a[i] + a[j]
                aim = target - sum
                if aim in pairs:
                    w = i
                    x = j
                    y = pairs[aim][0]
                    z = pairs[aim][1]
                    if len(set([w, x, y, z])) == 4:
                        r = [w, x, y, z]
                        r.sort()
                        return r
                else:
                    pairs[sum] = (i, j)
    return None

n, target = map(int, input().split())
a = list(map(int, input().split()))

result = find(a, target)
if result:
    print(result[0] + 1, result[1] + 1,1 + result[2],1 + result[3])
else:
    print("IMPOSSIBLE")
