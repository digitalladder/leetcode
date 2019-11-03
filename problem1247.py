#problem 1247 / minimum swaps to make strings equal
class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if len(s1) != len(s2):
            return -1
        xy = 0
        yx = 0
        res = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    xy += 1
                else:
                    yx += 1
        if (xy%2) != (yx%2):
            return -1
        res = xy//2+yx//2+(xy%2)*2
        return res