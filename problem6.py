#problem 6 / zigzag conversion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        row = 0
        direction = 1
        zout = ['']*numRows
        for i in range(len(s)):
            zout[row] += s[i]
            if numRows > 1:
                row += direction
                if row == 0 or row == numRows-1:
                    direction *= -1
        res = ''.join(zout)
        return res