class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        up = True
        i = 0
        j = 0
        m = len(mat)
        n = len(mat[0])
        
        while len(res) != m * n:
            if up:
                while 0 <= i < m and 0 <= j < n:
                    res.append(mat[i][j])
                    i -= 1
                    j += 1
                if i == -1 and j < n:
                    i = 0
                elif j == n:
                    i += 2
                    j -= 1
                up = False
            else:
                while 0 <= i < m and 0 <= j < n:
                    res.append(mat[i][j])
                    i += 1
                    j -= 1
                if j == -1 and i < m:
                    j = 0
                elif i == m:
                    j += 2
                    i -= 1
                up = True
        return res