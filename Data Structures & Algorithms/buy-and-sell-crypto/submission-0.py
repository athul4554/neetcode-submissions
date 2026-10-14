class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_v = prices[0]
        for i in prices:
            if i<min_v:
                min_v=i
                continue
            profit = max(profit,i-min_v)
        return profit