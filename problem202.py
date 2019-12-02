#problem 202 / happy number
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getnext(n):
            total = 0
            while n > 0:
                d = n%10
                n = n//10
                total += d**2
            return total
        
        cache = set()
        while n != 1 and n not in cache:
            cache.add(n)
            n = getnext(n)
        return n == 1