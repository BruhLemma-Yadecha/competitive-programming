# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1]) # amount gained by sending to city A instead of B
        
        total_cost = 0
        n = len(costs) // 2
        # Sum the first half for city A and the second half for city B
        for i in range(n):
            total_cost += costs[i][0] + costs[i + n][1]
        
        return total_cost