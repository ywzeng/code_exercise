class Solution_DP_with_Extra_Space:
    def maxProfit(self, prices: List[int]) -> int:
        """ DP without maintaining extra lists, namely the space complexity of O(1). """
        current_cash = 0
        current_stock = -prices[0]      # The cash after buying stock.

        for i in range(1, len(prices)):
            temp_cash = max(current_cash, current_stock+prices[i])      # sell
            temp_stock = max(current_stock, current_cash-prices[i])        # buy
            current_cash, current_stock = temp_cash, temp_stock
        return current_cash


class Solution_DP:
    def maxProfit(self, prices: List[int]) -> int:
        """ DP """
        # dp[i][0] represents the cash when has no stock, dp[i][1] represents the cash when has stock.
        dp_list = [[0, 0] for i in range(len(prices))]
        dp_list[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp_list[i][0] = max(dp_list[i-1][0], dp_list[i-1][1]+prices[i])       # no stock, so still not buy or sell the stock.
            dp_list[i][1] = max(dp_list[i-1][1], dp_list[i-1][0]-prices[i])       # has stock, so the stock is buying before or buying today.
        return dp_list[-1][0]


class Solution_Greedy:
    def maxProfit(self, prices: List[int]) -> int:
        """ If today's price is lower than the next's price, we can buy on today and sell on the next day. """
        total_profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                total_profit += prices[i+1]-prices[i]
        return total_profit
