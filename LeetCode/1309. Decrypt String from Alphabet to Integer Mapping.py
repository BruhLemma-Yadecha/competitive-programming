class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(s):
            current_char = s[i]
            # attempt to look ahead
            j = i + 2
            if j < len(s):
                if s[j] == '#':
                    number = int(s[i:j])
                    letter = to_letter(number)
                    result.append(letter)
                    i += 3
                    continue
            # no hashtag or end of string
            letter = to_letter(int(current_char))
            result.append(letter)
            i += 1

        return ''.join(result)
def to_letter(n):
    return chr(ord('a') + n - 1)
