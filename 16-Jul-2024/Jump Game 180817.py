# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        for i in range(len(nums)):
            if i > pos:
                return False
            pos = max(pos, i + nums[i])
            
        return True