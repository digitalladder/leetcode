#problem 322 / coin change
#mameroy
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 1:
            return 0
        cache = {}
        count = self.helper(coins,amount,cache)
        if count == float('inf'):
            return -1
        return count
        
    def helper(self,coins,amount,cache):
        if amount == 0:
            return 0
        if amount in cache:
            return cache[amount]
        cache[amount] = float('inf')
        for coin in coins:
            if amount-coin >=0:
                cache[amount] = min(cache[amount],self.helper(coins,amount-coin,cache)+1)
        return cache[amount]
            
#Bottom up 
## much faster
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = amount + 1
        dp = [MAX]*MAX
        dp[0] = 0
        for i in xrange(1, MAX):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return -1 if dp[amount] > amount else dp[amount]