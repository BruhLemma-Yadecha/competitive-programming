class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        index_ref = {}
        for index, value in enumerate(nums):
            index_ref[value] = index
        for i, j in operations:
            target_index = index_ref[i]
            nums[target_index] = j
            index_ref[j] = target_index
        return nums 
        
        