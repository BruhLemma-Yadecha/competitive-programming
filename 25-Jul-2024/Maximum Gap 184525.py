# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        smallest, largest = min(nums), max(nums)
        if smallest == largest:
            return 0
        
        bucket_size = max(1, (largest - smallest) // (n - 1))
        bucket_count = (largest - smallest) // bucket_size + 1
        
        buckets = [[None, None] for _ in range(bucket_count)]
        
        for num in nums:
            idx = (num - smallest) // bucket_size
            if not buckets[idx][0]:
                buckets[idx][0] = buckets[idx][1] = num
                
            buckets[idx][0] = min(buckets[idx][0], num) # left bound
            buckets[idx][1] = max(buckets[idx][1], num) # right bound
        
        max_gap = 0
        prev_max = smallest
        for bucket in buckets:
            if bucket[0] is None:
                continue # empty bucket
            max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1] # inter-bucket gap
        
        return max_gap