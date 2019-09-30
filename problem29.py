#problem 29 / divide two integers
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend<0)==(divisor<0)
        a = abs(dividend)
        b = abs(divisor)
        res = 0
        while a >= b:
            x = 0
            while a >= b << (x + 1): x += 1
            res += 1 << x
            a -= b << x
        return min(res if sign else -res, 2147483647)