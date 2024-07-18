# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        replacements = 0
        max_allowed = nums[-1]

        for i in range(n - 2, -1, -1):
            curr = nums[i]
            if curr > max_allowed:
                # Calculate the number of parts the current element needs to be split into.
                num_parts = (curr + max_allowed - 1) // max_allowed
                replacements += num_parts - 1  # Subtract 1 because the element itself counts as one part.
                max_allowed = curr // num_parts
            else:
                max_allowed = curr

        return replacements