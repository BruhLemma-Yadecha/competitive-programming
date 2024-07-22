# Problem: D - Playlist - https://codeforces.com/gym/536373/problem/D

from collections import namedtuple
import heapq

n, k = map(int, input().split())
songs = []
song = namedtuple('song', ('length', 'beauty'))
for _ in range(n):
    l, b = map(int, input().split())
    songs.append(song(l, b))

# Sort songs by beauty in descending order
songs.sort(key=lambda x: -x.beauty)

max_pleasure = 0
lengths_heap = []
current_length_sum = 0

for s in songs:
    # Add current song's length to the sum and the min-heap
    heapq.heappush(lengths_heap, s.length)
    current_length_sum += s.length
    
    # Ensure only k most beautiful songs are considered
    if len(lengths_heap) > k:
        current_length_sum -= heapq.heappop(lengths_heap)
    
    max_pleasure = max(max_pleasure, s.beauty * current_length_sum)

print(max_pleasure)