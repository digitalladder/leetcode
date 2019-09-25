#problem 123 / best time to buy and sell stock III
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0]*n for i in range(3)] 
        for i in range(1,3):
            balance = -prices[0]
            for j in range(1,n):
                dp[i][j] = max(dp[i][j-1],balance+prices[j])
                balance = max(balance,dp[i-1][j-1]-prices[j])
        return dp[2][n-1]