class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lesser = [x for x in nums if x < pivot]
        equal = [x for x in nums if x == pivot]
        greater = [x for x in nums if x > pivot]
        return lesser + equal + greater
        