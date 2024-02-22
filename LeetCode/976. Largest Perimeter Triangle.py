class Solution(object):
    def triangle(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            return False
        return True
    
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if self.triangle(nums[i], nums[i+1], nums[i+2]):
                return nums[i] + nums[i+1] + nums[i+2]
        return 0


        