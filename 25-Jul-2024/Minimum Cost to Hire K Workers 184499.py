# Problem: Minimum Cost to Hire K Workers - https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        heap = []
        n = len(quality)
        
        def wage_quality_ratio(worker_index):
            return wage[worker_index] / quality[worker_index]
        
        workers = sorted(range(n), key=wage_quality_ratio)
        
        res = float('inf')
        quality_sum = 0
        for worker in workers:
            heapq.heappush(heap, -quality[worker])
            quality_sum += quality[worker]
            if len(heap) > k:
                quality_sum += heapq.heappop(heap)
            if len(heap) == k:
                res = min(res, quality_sum * wage_quality_ratio(worker))
                
        return res