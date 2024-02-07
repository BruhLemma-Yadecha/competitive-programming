class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # using 3i + 3 = num
        i = (num - 3) // 3
        j = i + 1
        k = i + 2

        # accounting for i being a float
        if i + j + k == num:
            return [i, j, k]
        else:
            return []
        