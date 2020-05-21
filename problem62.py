# problem 62 / unique paths
# dp
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [0]*(m+1)
        dp[1] = 1
        for i in range(n):
            for j in range(1,m+1):
                dp[j] = dp[j-1]+dp[j]
            print(dp)
        return dp[-1]