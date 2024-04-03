n = int(input())
s = input()
# shortest subsequence that has every element
elements = set(list(s))
m = len(elements)

freq = {}
i = 0
res = 1_000_000_000_000

for j in range(n):
    freq[s[j]] = freq.get(s[j], 0) + 1
    if len(freq) == m:
        # shrink i as much as possible
        while len(freq) == m:
            res = min(res, j - i + 1)
            
            if freq[s[i]] == 1:
                del freq[s[i]]
            else:
                freq[s[i]] -= 1
            i += 1
print(res)
        