class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = -1
        i = 0
        j = 0
        m = len(grid)
        n = len(grid[0])
        while i < m - 2:
            # slide across a row
            while j < n - 2:
                # create hourglass
                hourglass = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                hourglass += grid[i + 1][j + 1]
                hourglass += grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                max_sum = max(max_sum, hourglass)
                j += 1
            j = 0
            i += 1
        return max_sum
