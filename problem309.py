#problem 309 / best time to buy and sell stock with cooldown
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        if n < 2:
            return 0
        buy = [0]*n
        sell = [0]*n
        buy[0] = -prices[0]
        for i in range(1,n):
            if i <= 2:
                buy[i] = max(-prices[i],buy[i-1])
            else:
                buy[i] = max(sell[i-2]-prices[i],buy[i-1])
            sell[i] = max(buy[i-1]+prices[i],sell[i-1])
        return sell[n-1]

# with O(1) space
def maxProfit(self, prices):
    if len(prices) < 2:
        return 0
    sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
    for price in prices:
        prev_buy = buy
        buy = max(prev_sell - price, prev_buy)
        prev_sell = sell
        sell = max(prev_buy + price, prev_sell)
    return sell