class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        DP
        Add some conditional judgments to verify whether the current position is reachable.
        Namely, determine whether the current, the above and the left positions are blocked by obstacles.
        """
        if obstacleGrid[0][0] == 1:
            return 0

        dp_list = [[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        # Fill the first row and the first column.
        dp_list[0][0] = 1
        for i in range(1, len(obstacleGrid[0])):
            dp_list[0][i] = -1 if obstacleGrid[0][i] == 1 or dp_list[0][i-1] == -1 else 1
        for i in range(1, len(obstacleGrid)):
            dp_list[i][0] = -1 if obstacleGrid[i][0] == 1 or dp_list[i-1][0] == -1 else 1
        
        for i in range(1, len(obstacleGrid)):       # Row
            for j in range(1, len(obstacleGrid[i])):        # Column
                if obstacleGrid[i][j] == 1 or (dp_list[i][j-1] == -1 and dp_list[i-1][j] == -1):
                    dp_list[i][j] = -1
                elif dp_list[i][j-1] > 0 and dp_list[i-1][j] > 0:
                    dp_list[i][j] = dp_list[i][j-1] + dp_list[i-1][j]
                else:
                    dp_list[i][j] = dp_list[i][j-1] if dp_list[i][j-1] > 0 else dp_list[i-1][j]
        return dp_list[-1][-1] if dp_list[-1][-1] > 0 else 0
