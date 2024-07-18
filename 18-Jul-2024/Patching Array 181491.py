# Problem: Patching Array - https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr = 1
        patches = 0
        
        i = 0
        while curr <= n:
            if i < len(nums) and nums[i] <= curr:
                curr += nums[i]
                i += 1
            else:
                curr *= 2
                patches += 1
        return patches