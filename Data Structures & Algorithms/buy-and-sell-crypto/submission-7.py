class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        [10,1,5,6,7,1]
        # start at 10 and 1
        # if profit increases, move r, else l
        l,r,max_profit = 0,1,0
        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_profit