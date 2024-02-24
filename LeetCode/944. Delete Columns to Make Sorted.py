class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res = 0
        columns = [[row[i] for row in strs] for i in range(len(strs[0]))]
        for col in columns:
            if sorted(col) != col:
                res += 1
        return resz