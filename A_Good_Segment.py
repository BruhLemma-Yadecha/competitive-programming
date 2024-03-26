n = int(input())
s = input()

i, longest = 0, 0
while i < n:
    cursor = ord(s[i])
    j = i + 1
    while j < n:
        if ord(s[j]) == cursor + 1:
            cursor += 1
        else:
            break
        j += 1
    longest = max(longest, j - i)
    i += 1
print(longest)
