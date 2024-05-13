t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    
    # what's the damage of each attack? Either lasts until the next one or k
    def damage(attack_index, k):
        if attack_index == n - 1:
            return k
        return min(k, a[attack_index + 1] - a[attack_index])
    def total_damage(k):
        res = 0
        for i in range(len(a)):
            res += damage(i, k)
        return res
    
    # now do a binary search between 1 and the dragon's health h
    l = 1
    r = h
    while l < r:
        mid = (l + r) // 2
        if total_damage(mid) >= h:
            r = mid
        else:
            l = mid + 1
    print(l)