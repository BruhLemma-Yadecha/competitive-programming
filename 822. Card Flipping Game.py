class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        numbers = set()
        blacklist = set()
        for i, j in zip(fronts, backs):
            if i != j:
                numbers.add(i)
                numbers.add(j)
            else:
                blacklist.add(i)
        numbers = numbers.difference(blacklist)
        if len(numbers) == 0:
            return 0
        else:
            return min(numbers)
        