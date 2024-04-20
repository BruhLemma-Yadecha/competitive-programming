class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        count = 0
        even = sum(nums[::2])
        odd = sum(nums[1::2])
        even_sum = 0
        odd_sum = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                even -= nums[i]
            else:
                odd -= nums[i]
            if even_sum + odd == odd_sum + even:
                count += 1
            if i % 2 == 0:
                even_sum += nums[i]
            else:
                odd_sum += nums[i]
        return count
