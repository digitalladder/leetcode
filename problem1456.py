# problem 1456 / maximum number of vowels in a substring of given length
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = 0
        res = 0
        total = 0
        for j in range(len(s)):
            if j < k:
                if s[j] in {'a','e','i','o','u'}:
                    total += 1
            else:
                if s[j] in {'a','e','i','o','u'}:
                    total += 1
                if s[i] in {'a','e','i','o','u'}:
                    total -= 1
                i += 1
            res = max(res,total)
        return res