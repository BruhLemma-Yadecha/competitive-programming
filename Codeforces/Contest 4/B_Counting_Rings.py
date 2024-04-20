run = 0
s = input()
i = 0
while i < len(s):
    if s[i] == 'O':
        # start of run
        j = i
        while j < len(s) and s[j] == 'O':
            j += 1
        run = max(run, j - i)
        i = j  # Update i to the end of the current run
    else:
        i += 1
print(run)
