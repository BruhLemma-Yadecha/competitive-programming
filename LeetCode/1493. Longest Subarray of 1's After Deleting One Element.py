class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        maxLength = 0
        zeroes = 0

        while right < len(nums):
            if nums[right] == 0:
                zeroes += 1

            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            maxLength = max(maxLength, right - left)
            right += 1

        return maxLength
