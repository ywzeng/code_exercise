class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        DP
        In addition to the first row and the first column, the steps on remaining indexes depend on its above and left indexes.
        Namely, dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j].
        """
        dp_list = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]

        # Fill in the first row and the first column with original step value.
        dp_list[0][0] = grid[0][0]
        for i in range(1, len(grid[0])):        # First row.
            dp_list[0][i] = dp_list[0][i-1] + grid[0][i]
        for i in range(1, len(grid)):       # First column.
            dp_list[i][0] = dp_list[i-1][0] + grid[i][0]
        for i in range(1, len(grid)):       # Row
            for j in range(1, len(grid[i])):        # Column
                dp_list[i][j] = min(dp_list[i-1][j], dp_list[i][j-1]) + grid[i][j]
        return dp_list[-1][-1]
