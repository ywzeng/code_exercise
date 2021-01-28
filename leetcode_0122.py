class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ If today's price is lower than the next's price, we can buy on today and sell on the next day. """
        total_profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                total_profit += prices[i+1]-prices[i]
        return total_profit
