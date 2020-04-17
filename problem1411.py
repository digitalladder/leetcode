#problem 1411 / number of ways to paint Nx3 grid
# Two patterns for each row: 121 and 123.
# We consider the state of the first row,
# pattern 121: 121, 131, 212, 232, 313, 323.
# pattern 123: 123, 132, 213, 231, 312, 321.
# So we initialize a121 = 6, a123 = 6.

# We consider the next possible for each pattern:
# Patter 121 can be followed by: 212, 213, 232, 312, 313
# Patter 123 can be followed by: 212, 231, 312, 232
# 121 => two 121, three 123
# 123 => two 121, two 123
# So we can write this dynamic programming transform equation:
# b121 = a121 * 3 + a123 * 2
# b123 = a121 * 2 + a123 * 2

class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        aba = 6
        abc = 6
        for i in range(2,n+1):
            temp = aba
            aba = aba*3+abc*2
            abc = temp*2+abc*2
        return (aba+abc)%(10**9+7)