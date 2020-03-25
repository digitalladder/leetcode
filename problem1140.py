#problem1140 / stone game II
# bottom up
class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        remain = [0]*(n+1)
        for i in range(n-1,-1,-1):
            remain[i] = remain[i+1]+piles[i]
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(1,n+1):
                if i+2*j >= n:
                    dp[i][j] = remain[i]
                for k in range(1,2*j+1):
                    if i+k > n:
                        break
                    dp[i][j] = max(dp[i][j],remain[i]-dp[i+k][max(j,k)])
        
        return dp[0][1]

#top down(memorize)
class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        cache = {}
        remain = [0]*(n+1)
        for i in range(n-1,-1,-1):
            remain[i] = remain[i+1]+piles[i]
        
        def dfs(index,m):
            if index+2*m >= n:
                return remain[index]
            if (index,m) in cache:
                return cache[(index,m)]
            temp = 0
            for k in range(1,2*m+1):
                if index+k > n:
                    break
                temp = max(temp,remain[index]-dfs(index+k,max(k,m)))
            cache[(index,m)] = temp
            return cache[(index,m)]
        return dfs(0,1)