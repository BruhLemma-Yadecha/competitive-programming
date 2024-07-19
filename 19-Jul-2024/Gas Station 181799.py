# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start at zero and move the start back if you encounter an issue
        tank = 0
        start = curr = 0
        path_length = 0
        n = len(gas)
        while path_length != n:
            path_length += 1
            tank += gas[curr]
            if cost[curr] > tank:
                while tank < cost[curr]:
                    # move the start one step back
                    start = n - 1 if start == 0 else start - 1
                    if start == curr:
                        return -1
                    tank += gas[start] - cost[start]
                    path_length += 1
            tank -= cost[curr]
            curr = 0 if curr == n - 1 else curr + 1
        return start
                     