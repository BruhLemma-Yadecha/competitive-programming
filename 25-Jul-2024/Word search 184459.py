# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # find all of the starting positions
        starts = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    starts.append((i, j))
                    
        rows = len(board)
        columns = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def valid(i, j):
            return i >= 0 and i < rows and j >= 0 and j < columns
                
        def explore(i, j, idx, visited):
            if idx == len(word):
                return True
            
            for d in directions:
                new_i, new_j = i + d[0], j + d[1]
                if valid(new_i, new_j) and \
                (new_i, new_j) not in visited and \
                board[new_i][new_j] == word[idx]:
                    visited.add((new_i, new_j))
                    if explore(new_i, new_j, idx + 1, visited):
                        return True
                    visited.remove((new_i, new_j))
            
            return False
        
        for start in starts:
            if explore(start[0], start[1], 1, {start}):
                return True
        
        return False