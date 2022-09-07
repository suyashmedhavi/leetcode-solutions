# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, minPrice = 0, prices[0]
        for i in range(1, len(prices)):
            ans = max(ans, prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
        return ans

