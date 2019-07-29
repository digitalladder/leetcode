#problem 13 / roman to interger
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        pairs = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        p = 'I'
        for l in s[::-1]:
            if pairs[l] < pairs[p]:
                number -= pairs[l]
            else:
                number += pairs[l]
            p = l
        return number