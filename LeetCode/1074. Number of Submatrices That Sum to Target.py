from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        pre = self.prefix_sum_2d(matrix)
        
        # go through the prefix sum matrix and try to find the target by shrinking the submatrix
        # matrix is of the form i for the top row we aren't considering
        #  k, l for the bottom right corner
        count = 0
        for i in range(n):
            for k in range(i, n): # start from a row and expand downwards
                # store the columns visited as we go so we can check if current_col - target has been seen before
                columns_seen = {0: 1}
                for l in range(m):
                    current_col = pre[k + 1][l + 1] - pre[i][l + 1]
                    # if the sum - target is in the columns_seen, then we find a submatrix that sums to target
                    if current_col - target in columns_seen:
                        count += columns_seen[current_col - target] # as we may have seen more than one
                    columns_seen[current_col] = columns_seen.get(current_col, 0) + 1 # memorize for later
        return count
    
    def prefix_sum_2d(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

        return prefix_sum