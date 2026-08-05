class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=10000000000000000000000000000000000000
        
        n=len(prices)
        for i in range(n):
            buy=min(buy,prices[i])
            profit=max(profit,prices[i]-buy)
        return profit