#problem 1292 maximum side length of a square with sum less than or equal to threshold
class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        if not mat:
            return 0
        max_square = 0
        dp = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        res,side = 0,1
        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]
                while i >= side and j >= side and dp[i][j]-dp[i-side][j]-dp[i][j-side]+dp[i-side][j-side] <= threshold:
                    res = side
                    side += 1
        return res