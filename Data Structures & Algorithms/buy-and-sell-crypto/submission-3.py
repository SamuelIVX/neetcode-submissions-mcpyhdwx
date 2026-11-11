class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        min_price = float('inf')

        for low in range(len(prices)):
            min_price = min(min_price, prices[low])
            maxx = max(maxx, prices[low] - min_price)
        
        return maxx