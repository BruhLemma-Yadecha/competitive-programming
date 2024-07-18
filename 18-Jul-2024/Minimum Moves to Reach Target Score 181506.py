# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        curr = target
        moves = 0
        while maxDoubles > 0 and curr != 1:
            if curr % 2 == 1:
                moves += 1
                curr -= 1
            if curr == 1:
                return moves
            curr /= 2
            maxDoubles -= 1
            moves += 1
            
        return int(moves + curr - 1)