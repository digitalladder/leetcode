#problem 1000 / minimum cost to merge stones
class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        n = len(stones)
        if (n-1)%(K-1) != 0:
            return -1
        presum = [0]*(n+1)
        cache = {}
        for i in range(n):
            presum[i+1] = presum[i]+stones[i]
            
        def dp(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if j-i+1 < K:
                return 0
            res = min(dp(i,mid)+dp(mid+1,j) for mid in range(i,j,K-1))
            if (j-i)%(K-1) == 0:
                res += presum[j+1]-presum[i]
            cache[(i,j)] = res
            return res
        
        return dp(0,n-1)