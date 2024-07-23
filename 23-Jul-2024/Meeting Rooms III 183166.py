# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

from typing import List
from heapq import heappop, heappush

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        end_times = [(0, i) for i in range(n)]
        uses = [0] * n
        meetings.sort()
        for start, end in meetings:
            newly_freed = []
            while end_times and end_times[0][0] <= start:
                _, node = heappop(end_times)
                newly_freed.append(node)
                
            for node in newly_freed:
                heappush(end_times, (0, node))
                
            old_end, room = heappop(end_times)
            duration = end - start
            new_start = max(old_end, start)
            new_end = new_start + duration
            heappush(end_times, (new_end, room))
            uses[room] += 1
        return max(range(n), key=lambda x: uses[x])