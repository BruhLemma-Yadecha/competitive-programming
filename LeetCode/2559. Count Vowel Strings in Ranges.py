from typing import List

class Solution:
    def __init__(self) -> None:
        self.vowels = set('aeiou')
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pre = [0 for _ in range(len(words) + 1)]
        for i in range(1, len(words) + 1):
            pre[i] = pre[i - 1] + self.valid(words[i - 1])
        print(*pre)
        query_responses = [pre[right + 1] - pre[left] for left, right in queries]
        return query_responses
        
    def valid(self, s: str) -> bool:
        return s[0] in self.vowels and s[-1] in self.vowels