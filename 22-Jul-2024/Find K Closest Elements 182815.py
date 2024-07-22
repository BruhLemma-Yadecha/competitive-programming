# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = defaultdict(list)
        for y in arr:
            locdiff = abs(x - y)
            diff[locdiff].append(y)
        res = []
        # print(diff)
        keys = sorted(list(diff.keys()))
        for ky in keys:
            if len(res) == k:
                break
            v = sorted(diff[ky])
            for i in v:
                if len(res) == k:
                    break
                res.append(i)
            
        return sorted(res)
            