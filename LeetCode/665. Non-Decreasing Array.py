class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # two pointers approach
        changes = 0
        i = 1
        while i < len(nums):
            if nums[i - 1] > nums[i]:
                changes += 1
                # check for an early exit
                if changes > 1:
                    return False
                
                # check if you're near the left border
                # or look back to the element even before that for corrections
                if i == 1 or nums[i] >= nums[i - 2]:
                    # if the second case is true, you can simply yank down i - 1 to align it to i
                    nums[i - 1] = nums[i]
                else:
                    # if then nums[i - 2] > nums[i], fix nums[i]
                    nums[i] = nums[i - 1]
            i += 1
        return True