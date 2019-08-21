#problem 50 / pow(x,n)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        res = 1
        pro = x
        while n > 0:
            if n%2 == 1:
                res = res*pro
            pro = pro*pro
            n = n//2
        return res