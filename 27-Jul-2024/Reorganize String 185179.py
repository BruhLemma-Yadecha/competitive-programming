# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:   
        heap = []
        for letter, letter_freq in Counter(s).items():
            heappush(heap, (-letter_freq, letter))
        res = []
        while heap:
            if not res:
                freq, c = heappop(heap)
                res.append(c)
                if freq + 1 < 0:
                    heappush(heap, (freq + 1, c))
            else:
                temp = []
                while heap:
                    if len(heap) == 1 and heap[0][1] == res[-1]:
                        return ''
                    freq, c = heappop(heap)
                    if c != res[-1]:
                        res.append(c)
                        if freq + 1 < 0:
                            heappush(heap, (freq + 1, c))
                        break
                    else:
                        temp.append((freq, c))
                for f, c in temp:
                    heappush(heap, (f, c))
        return ''.join(res)