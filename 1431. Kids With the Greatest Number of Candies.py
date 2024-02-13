class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        greatest = max(candies)
        for j in candies:
            if extraCandies + j >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result
        