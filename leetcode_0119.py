class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        The k-th row has k+1 elements (k starts from 0).
        DP.
        When calculating the 0-th row, the dp list is [1, ...].
        When calculating the 1-th row, the dp list is [1, 1, ...].
        When calculating the 2-th row, the dp list is [1, 2, 1, ...].
        That is, alter the dp list dynamically.
        In order not to change the number of target index before calculating it, we can calculate the dp_list from the tail to the front.
        Specifically, dp_list[j] = dp_list[j] + dp_list[j-1].
        """
        dp_list = [0 for i in range(rowIndex+1)]
        dp_list[0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i, -1, -1):
                if j == 0 or j == i:
                    dp_list[j] = 1
                else:
                    dp_list[j] = dp_list[j] + dp_list[j-1]
        return dp_list
