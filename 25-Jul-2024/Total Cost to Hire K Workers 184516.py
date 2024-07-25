# Problem: Total Cost to Hire K Workers - https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

class Solution:
    def totalCost(self, costs, k, candidates):
        l_bound, r_bound = 0, len(costs) - 1
        l_heap, r_heap = [], []

        cost = 0
        for _ in range(k):
            while len(l_heap) < candidates and l_bound <= r_bound:
                heapq.heappush(l_heap, costs[l_bound])
                l_bound += 1
                
            while len(r_heap) < candidates and l_bound <= r_bound:
                heapq.heappush(r_heap, costs[r_bound])
                r_bound -= 1
            if l_heap and (not r_heap or l_heap[0] <= r_heap[0]):
                cost += heapq.heappop(l_heap)
            else:
                cost += heapq.heappop(r_heap)
                
        return cost