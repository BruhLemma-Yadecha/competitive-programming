from collections import defaultdict

n,s=map(int, input().split())
a=list(map(int, input().split()))
i,j,res=0,0,0
freq = defaultdict(int)
for j in range(n):
    freq[a[j]] += 1
    while len(freq) > s:
        freq[a[i]] -= 1
        if freq[a[i]] == 0:
            del freq[a[i]]
        i += 1
    res += j - i + 1
print(res)