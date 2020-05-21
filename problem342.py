#problem 342 / power of four
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        div = 4
        while div*div <= num:
            div *= div
        while div*4 <= num:
            div *= 4
        if div == num:
            return True
        return False

# bit manipulate
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0