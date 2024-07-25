# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        ASCII_ZERO = 48
        def mapping_equivalent(x):
            val = 0
            for c in str(x):
                val += mapping[ord(c) - ASCII_ZERO]
                val *= 10
            return val
        nums.sort(key=lambda x: mapping_equivalent(x))
        return nums