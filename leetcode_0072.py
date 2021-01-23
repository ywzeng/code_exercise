class Solution_quick:
    def minDistance(self, word1: str, word2: str) -> int:
        def reverse_dp(i: int, j: int, dp_dict: dict) -> int:
            """
            Recursively calculate the dp value from (i, j) to (0, 0).
            Use Dict to store the dp value, where key is the tuple (i, j), value is the dp value of (i, j).
            i represents row index, and j represents column index.
            """
            if (i, j) in dp_dict:
                return dp_dict[(i, j)]
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            if word1[i] == word2[j]:
                dp_dict[(i, j)] = reverse_dp(i-1, j-1, dp_dict)
            else:
                dp_dict[(i, j)] = 1 + min(reverse_dp(i-1, j, dp_dict), reverse_dp(i, j-1, dp_dict), reverse_dp(i-1, j-1, dp_dict))
            return dp_dict[(i, j)]
        
        dp_dict = {}
        return reverse_dp(len(word1)-1, len(word2)-1, dp_dict)


class Solution_slow:
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
