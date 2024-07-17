# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ref = {}
        left = 0
        right = 0
        max_len = 0
        
        while right < len(s):
            if s[right] in ref:
                left = max(ref[s[right]] + 1, left)
            
            ref[s[right]] = right
            max_len = max(max_len, right - left + 1)
            right += 1
            
        return max_len