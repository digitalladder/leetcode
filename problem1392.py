#problem 1392 / longest happy prefix
#rolling hash
class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, l, r, mod = 0, 0, 0, 10**9 + 7
        for i in range(len(s) - 1):
            l = (l * 128 + ord(s[i])) % mod
            r = (r + pow(128, i, mod) * ord(s[~i])) % mod
            if l == r: res = i + 1
        return s[:res]

#can use kmp algorithm