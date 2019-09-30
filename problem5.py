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