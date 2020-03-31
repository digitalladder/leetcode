#problem 562 / longest line of consecutive one in matrix
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0:
            return 0
        n = len(M)
        m = len(M[0])
        dp = [[[0]*m for i in range(n)] for j in range(4)]
        ones = 0
        for i in range(n):
            for j in range(m):
                if M[i][j] == 1:
                    dp[0][i][j] = dp[0][i][j-1]+1 if j > 0 else 1
                    dp[1][i][j] = dp[1][i-1][j]+1 if i > 0 else 1
                    dp[2][i][j] = dp[2][i-1][j-1]+1 if (i > 0 and j > 0) else 1
                    if i > 0 and j < m-1:
                        dp[3][i][j] = dp[3][i-1][j+1]+1
                    else:
                        dp[3][i][j] = 1
                    ones = max(ones,dp[0][i][j],dp[1][i][j],dp[2][i][j],dp[3][i][j])
        return ones