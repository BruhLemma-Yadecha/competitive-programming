# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        
        # Use as many 1s as possible, up to k
        ones_used = min(numOnes, k)
        res += ones_used
        k -= ones_used
        
        # Use as many zeroes as possible to not reduce the sum
        k -= min(numZeros, k)
        
        # Use remaining capacity for -1s
        res -= min(numNegOnes, k)
        
        return res