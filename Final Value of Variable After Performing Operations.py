class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        legend = {
            "++X" : 1,
            "X++" : 1,
            "--X" : -1,
            "X--": -1
        }
        x = 0
        for operation in operations:
            x += legend[operation]
        return x