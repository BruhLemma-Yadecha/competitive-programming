class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l = 201
        shortest = ""
        for s in strs:
            if len(s) < l:
                shortest = s
                l = len(s)
        r = ""
        for i in range(0, l):
            valid = True
            for s in strs:
                if s[i] != shortest[i]:
                    valid = False
                    break
            if valid:
                r = r + shortest[i]
            else:
                break
        return r
        