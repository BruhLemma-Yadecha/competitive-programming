# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution(object):
    def largestPerimeter(self, nums: List[int]) -> int:
        def triangle(a: int, b: int, c:int) -> bool:
            if a + b <= c or a + c <= b or b + c <= a:
                return False
            return True
        
        nums.sort(reverse=True)
        
        for i in range(len(nums) - 2):
            if triangle(nums[i], nums[i+1], nums[i+2]):
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
        