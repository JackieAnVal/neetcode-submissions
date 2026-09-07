class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0] #7
        max_profit = 0
        for i in range(1, len(prices)):
            price = prices[i]
            min_buy = min(min_buy, price) #1
            max_profit = max(max_profit, price - min_buy) #4
        return max_profit