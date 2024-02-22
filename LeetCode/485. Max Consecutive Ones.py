class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_run = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                run_length = 0
                j = i
                while j < len(nums) and nums[j] == 1:
                    run_length += 1
                    j += 1
                max_run = max(max_run, run_length)
                i = j
            else:
                i += 1
        return max_run