class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for n in range(len(prices)):
            p = prices[n] - prices[l]
            if prices[n] < prices[l]:
                l = n
            profit = max(profit, p)

        return profit