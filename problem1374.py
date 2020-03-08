#problem 1374 / Generate a String With Characters That Have Odd Counts
class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n%2 == 1:
            return 'a'*n
        else:
            return 'a'*(n-1)+'b'