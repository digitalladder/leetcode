#problem 935 / knight dialer
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]
        MOD = 10**9+7
        dp = [1]*10
        for i in range(2,N+1):
            temp = [0]*10
            for j in range(10):
                for c in moves[j]:
                    temp[j] += dp[c]
                    temp[j] %= MOD
            dp = temp
        return sum(dp) % MOD