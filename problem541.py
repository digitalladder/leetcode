#problem 541 / reverse string II
#注意字符串下标，s[i:j]切片后，包括 s[i] 不包括 s[j]
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k >= len(s):
            return s[::-1]
        if k < len(s) <= 2*k:
            return s[k-1::-1]+s[k:]
        return self.reverseStr(s[:2*k],k)+self.reverseStr(s[2*k:],k)