#problem 1234 / replace the substring for balanced string
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        res = n = len(s)
        i = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while i < n and all(n / 4 >= count[c] for c in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res