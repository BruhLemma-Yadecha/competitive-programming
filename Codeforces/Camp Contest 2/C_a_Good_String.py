t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    def a_good(left, right, ascii):
        c = chr(ascii)
        if right - left == 1:
            if c == s[left]:
                return 0 # good as is
            else:
                return 1 # bad
        centre = (left + right) // 2
        on_the_left = s[left:centre].count(c)
        on_the_right = s[centre:right].count(c)
        
        sequence_length = right - left
        next_char = ascii + 1
        changes_if_left_picked = sequence_length // 2 - on_the_left
        changes_if_right_picked = sequence_length // 2 - on_the_right
        
        # now simply check if picking left or picking right would overall
        # reduce the amount of work
        return min(
            changes_if_left_picked + a_good(centre, right, next_char),
            changes_if_right_picked + a_good(left, centre, next_char)
        )
    print(a_good(0, n, ord('a')))