# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for idx, val in enumerate(strs):
            sorted_val = "".join(sorted(val))
            if sorted_val in res:
                res[sorted_val].append(val)
            else:
                res[sorted_val] = [val]
        return list(res.values())