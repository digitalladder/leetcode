#problem 121 /Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float("inf")     #表示正无穷大，负无穷为float("-inf")
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            elif price-minprice > maxprofit:
                maxprofit = price-minprice
        return maxprofit

#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minp = prices[0]
        maxpro = 0
        for i in range(1,len(prices)):
            if prices[i] < minp:
                minp = prices[i]
            else:
                maxpro = max(maxpro,prices[i]-minp)
        return maxpro