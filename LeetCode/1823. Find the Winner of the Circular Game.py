class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        p = [x for x in range(1, n + 1)]
        curr = 0
        while len(p) != 1:
            curr += k - 1
            if curr >= len(p):
                curr = curr % len(p)
            p[curr] = None
            p = [x for x in p if x != None]
        return p[0]