class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        DP
        Reserve one more row and column to represent the edit distance from '' to complete word1 and word2.
        The edit distance betwee '' and '' is 0.
        """
        # word1 length is row num, and word2 length is column num. Reserve one row and one column to represent the ''.
        dp = [[0 for i in range(len(word2)+1)] for i in range(len(word1)+1)]
        # Initialize the first row.
        for i in range(1, len(dp[0])):
            dp[0][i] = i
        # Initialize the first column.
        for i in range(1, len(dp)):
            dp[i][0] = i

        for i in range(1, len(dp)):     # Row, word1
            for j in range(1, len(dp[0])):      # Column, word2
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]-1)
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]
