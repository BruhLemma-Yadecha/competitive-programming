# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        res = []
        start = end = 0
        
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                # Found the end of a partition
                res.append(end - start + 1)
                start = i + 1
                
        return res