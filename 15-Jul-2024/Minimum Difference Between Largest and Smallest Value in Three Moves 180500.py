# Problem: Minimum Difference Between Largest and Smallest Value in Three Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        n = len(nums)
        
        res = nums[-1] - nums[0]
        for i in range(4):
            res = min(res, nums[n - 4 + i] - nums[i])
        return res