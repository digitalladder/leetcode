#problem 858 / mirror reflection
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(a,b):
            if a == 0:
                return b
            return gcd(b%a,a)
        g = gcd(p,q)        #lcm = p*q/g
        n = (p/g)%2         #n = lcm/q
        m = (q/g)%2         #m = lcm/p
        if n and m:
            return 1
        if n and not m:
            return 0
        if not n and m:
            return 2