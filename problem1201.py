#problem 1201 /ugly number III
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def gcd(a,b):
            if a == 0:
                return b
            return gcd(b%a,a)
        def lcm(a,b):
            return (a*b)//gcd(a,b)
        def cnt(val,a,b,c):
            return val//a + val//b + val//c -val//lcm(a, b)-val//lcm(a, c)-val//lcm(c, b) + val//lcm(lcm(a, b),c)
        lo = 1
        hi = min(a,b,c)*n
        while lo < hi:
            mid = lo+(hi-lo)//2
            if cnt(mid,a,b,c) < n:
                lo = mid+1
            else:
                hi = mid
        return lo