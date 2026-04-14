class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy, sell = 0,1
        while sell < len(prices):
            if prices[sell] - prices[buy] >= 0:
                profit = prices[sell] - prices[buy]
                res = max(res, profit)

            else: 
                buy = sell
            sell += 1

        return res        