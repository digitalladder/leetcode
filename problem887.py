#problem 887 / super egg drop
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[0]*(K+1) for i in range(N+1)]
        for m in range(1,N+1):
            for k in range(1,K+1):
                dp[m][k] = dp[m-1][k-1]+dp[m-1][k]+1
            if dp[m][K] >= N:
                return m

# 1D dynamic programming, reduce m dimension in dp
def superEggDrop(self, K, N):
        dp = [0, 0]
        m = 0
        while dp[-1] < N:
            for i in range(len(dp) - 1, 0, - 1):
                dp[i] += dp[i - 1] + 1
            if len(dp) < K + 1:
                dp.append(dp[-1])
            m += 1
        return m
#
class Solution(object):
    def superEggDrop(self, K, N):
        def f(x):
            ans = 0
            r = 1
            for i in range(1, K+1):
                r *= x-i+1
                r //= i
                ans += r
                if ans >= N: break
            return ans

        lo, hi = 1, N
        while lo < hi:
            mi = (lo + hi) // 2
            if f(mi) < N:
                lo = mi + 1
            else:
                hi = mi
        return lo