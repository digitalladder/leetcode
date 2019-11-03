#problem 139 / word break
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = {}
        def dfs(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            for i in range(start,len(s)+1):
                if s[start:i] in wordDict and dfs(i):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        return dfs(0)
## bfs(iterative)方法，利用 queue 记录 end 值，while 循环 pop ，遍历找可能的匹配单词（可能的end值）推入 queue

##自底向上
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [0]*(len(s)+1)
        dp[0] = 1
        for i in range(1,len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j] == 1:
                    dp[i] = 1
        if dp[len(s)] == 1:
            return True
        return False
