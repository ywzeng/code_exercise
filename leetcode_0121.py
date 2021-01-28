class Solution_better:
    def maxProfit(self, prices: List[int]) -> int:
        """ Still DP, but no need to explicitly maintaining a list. """
        min_buying_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < min_buying_price:
                min_buying_price = prices[i-1]
            temp_profit = prices[i]-min_buying_price
            if temp_profit > max_profit:
                max_profit = temp_profit
        return max_profit

    
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
