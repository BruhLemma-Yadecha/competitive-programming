#User function Template for python3

def isSubset( a1, a2, n, m):
    if m > n:
        return "No"
    in_a1 = {}
    in_a2 = {}
    for i in a1:
        if i in in_a1:
            in_a1[i] += 1
        else:
            in_a1[i] = 1
    for i in a2:
        if i in in_a2:
            in_a2[i] += 1
        else:
            in_a2[i] = 1
    for item, freq in in_a2.items():
        if item not in in_a1:
            return "No"
        if in_a1[item] < freq:
            return "No"
    return "Yes"
    
    

