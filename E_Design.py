n,q=list(map(int, input().split()))

# preprocess all of the prefixes and suffixes
prefixes = {}
suffixes = {}

index = 0
for _ in range(n):
    w = input()
    
    # process suffixes
    for i in range(len(w)):
        suffixes[w[i:]] = index

    # process prefixes
    for i in range(1, len(w) + 1):
        prefixes[w[:i]] = index
    
    index += 1

queries = []
for _ in range(q):
    pref, suff = input().split()
    if pref in prefixes and suff in suffixes:
        if prefixes[pref] == suffixes[suff]:
            print(prefixes[pref])
        else:
            print(-1)
    else:
        print(-1)