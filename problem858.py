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
        g = gcd(p,q)
        p = (p/g)%2
        q = (q/g)%2
        if p and q:
            return 1
        if p and not q:
            return 0
        if not p and q:
            return 2