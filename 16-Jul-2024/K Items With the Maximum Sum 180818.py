# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        
        from_ones = min(numOnes, k)
        res += from_ones
        k -= from_ones
        
        from_zeros = min(numZeros, k)
        k -= from_zeros
        
        from_neg_ones = min(numNegOnes, k)
        res += -1 * from_neg_ones
        k -= from_neg_ones
            
        return res