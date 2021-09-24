class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_ = 0
        for i in range(1,len(prices)) :
            
            profit += prices[i] - prices[i-1]
            max_ = max(profit,max_)
            if profit < 0 :
                profit = 0
        return max_
            