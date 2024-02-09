class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numbers = set()
        for i in nums:
            if i not in numbers:
                numbers.add(i)
            else:
                return True
        return False
        