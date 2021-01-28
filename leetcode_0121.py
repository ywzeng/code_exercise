class Solution_DP:
    def maxProfit(self, prices: List[int]) -> int:
        """
        DP.
        Profit is the selling prive minus the buying price.
        dp_list records the lowest buying price before that day.
        """
        dp_list = [0 for i in range(len(prices))]
        dp_list[0] = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            dp_list[i] = min(dp_list[i-1], prices[i-1])
            temp_profit = prices[i] - dp_list[i]
            max_profit = temp_profit if temp_profit > max_profit else max_profit 
        return max_profit
