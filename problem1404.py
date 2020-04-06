#problem 1404 / Number of Steps to Reduce a Number in Binary Representation to One
class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for ss in s:
            num = num*2+int(ss)
        count = 0
        while num != 1:
            if num%2 == 1:
                num += 1
            else:
                num /= 2
            count += 1
        return count