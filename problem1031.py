#problem 1031 / maximum sum of two non-overlapping subarrays
class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        n = len(A)
        pre = [0]*(n+1)
        pre[1] = A[0]
        for i in range(2,n+1):
            pre[i] = pre[i-1]+A[i-1]
        dp = [0]*(n+1)
        msum = [0]*(n+1)
        lsum = [0]*(n+1)
        for i in range(L+M):
            if i >= L:
                lsum[i] = max(lsum[i-1],pre[i]-pre[i-L])
            if i >= M:
                msum[i] = max(msum[i-1],pre[i]-pre[i-M])
        for i in range(L+M,n+1):
            lsum[i] = max(lsum[i-1],pre[i]-pre[i-L])
            msum[i] = max(msum[i-1],pre[i]-pre[i-M])
            dp[i] = max(dp[i-1],pre[i]-pre[i-L]+msum[i-L],lsum[i-M]+pre[i]-pre[i-M])
        return dp[-1]
        
##优化dp
def maxSumTwoNoOverlap(self, A, L, M):
        for i in xrange(1, len(A)):
            A[i] += A[i - 1]
        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
        for i in xrange(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
        return res