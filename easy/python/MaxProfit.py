'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''

class Solution():
    def maxProfit(self,prices):
        if not prices:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            p = prices[i]
            if p<minPrice:
                minPrice=p
            maxProfit = max(maxProfit,p-minPrice)
        return maxProfit


s = Solution()
assert 3 == s.maxProfit([2,1,4])
assert 5 == s.maxProfit([7, 1, 5, 3, 6, 4])
assert 0 == s.maxProfit([])
