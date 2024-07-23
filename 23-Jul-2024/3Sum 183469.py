# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            if nums[i] > 0: # impossible to get a sum of zero if there are no more zeroes or negatives
                break
            while j < k:
                loc = nums[i] + nums[j] + nums[k]
                if loc == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif loc < 0:
                    j += 1
                else:
                    k -= 1
        return list(res)