#problem 688 / knight probability in chessboard
from functools import lru_cache
class Solution: 
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        total = 8**K
        @lru_cache(maxsize=None)
        def dfs(k,r,c):
            if r<0 or r>N-1 or c<0 or c>N-1:
                return 0
            if k == 0:
                return 1 
            return dfs(k-1,r+2,c+1)+dfs(k-1,r+2,c-1)+dfs(k-1,r-2,c+1)+dfs(k-1,r-2,c-1)+dfs(k-1,r+1,c+2)+dfs(k-1,r+1,c-2)+dfs(k-1,r-1,c+2)+dfs(k-1,r-1,c-2)
        
        
        count = dfs(K,r,c)
        #print(dfs.cache_info())  #print lru_cache info
        return count/total

#自底向上
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = [[0] * N for _ in xrange(N)]
        dp[r][c] = 1
        for _ in xrange(K):
            dp2 = [[0] * N for _ in xrange(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2

        return sum(map(sum, dp))