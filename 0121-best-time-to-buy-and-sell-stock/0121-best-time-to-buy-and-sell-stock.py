class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mini = prices[0]
        max_profit = 0

        for price in range(1,n):
            cost = prices[price] - mini
            max_profit = max(max_profit, cost)
            mini = min(mini, prices[price])
        
        return max_profit
        