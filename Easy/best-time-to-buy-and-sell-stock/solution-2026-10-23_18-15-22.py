class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        res = 0 
        min_p = max(prices)

        for p in prices:
            res = max(res, p - min_p)
            min_p = min(p, min_p)
        
        return res