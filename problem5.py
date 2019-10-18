#problem 5 / longest palindromic substring
#dp
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        max_len = 0
        n = len(s)
        DP = [[0] * n for _ in xrange(n)]
        for i in xrange(n):
            DP[i][i] = True
            max_len = 1
            ans = s[i]
        for i in xrange(n-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = True
                ans = s[i:i+2]
                max_len = 2
        for j in xrange(n):
            for i in xrange(0, j-1):
                if s[i] == s[j] and DP[i+1][j-1]:
                    DP[i][j] = True
                    if max_len < j - i + 1:
                        ans = s[i:j+1]
                        max_len = j - i + 1
        return ans

#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        max_len = 0
        n = len(s)
        dp = [[0] * n for _ in xrange(n)]
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if i == j:
                    dp[i][j] == True
                elif j-i == 1 and s[i] == s[j]:
                    dp[i][j] ==True
                elif s[i] == s[i] and dp[i+1][j-1]:
                    dp[i][j] = True
                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    ans = s[i:j+1]
        return ans