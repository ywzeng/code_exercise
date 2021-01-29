class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """ DP """
        dp_list = [[0 for i in range(len(triangle))] for i in range(len(triangle))]
        dp_list[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j == 0:
                    dp_list[i][j] = dp_list[i-1][j] + triangle[i][j]
                elif j == i:
                    dp_list[i][j] = dp_list[i-1][j-1] + triangle[i][j]
                else:
                    dp_list[i][j] = min(dp_list[i-1][j-1], dp_list[i-1][j]) + triangle[i][j]
        return min(dp_list[-1])
