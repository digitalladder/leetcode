#problem 122 / best time to buy and sell stock II
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        i = j = 0
        res = 0
        while j+1 < len(prices):
            if prices[j] > prices[j+1]:
                res += prices[j]-prices[i]
                j += 1
                i = j
            else:
                j += 1
        res += prices[j]-prices[i]
        return res

#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        n = len(prices)
        for i in range(n-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1]-prices[i]
        return profit