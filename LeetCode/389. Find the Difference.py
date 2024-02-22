class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        chars = {}

        # add how many of each letter are in there
        for c in t:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        
        # subtract from the initial array so that the unique value will be left as 1
        for c in s:
            chars[c] -= 1
        for key in chars:
            if chars[key] == 1:
                return key