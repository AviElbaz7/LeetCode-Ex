class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        maxi = 0
        for i in range(1, len(prices)):
            maxi = max(maxi, prices[i] - low)
            low = min(low, prices[i])
        return maxi