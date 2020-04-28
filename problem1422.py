#problem 1422 / maximum score after splitting a string
# liner scan
#Result = Max of (ZerosOnLeft + OnesOnRight) = Max of (ZerosOnLeft + (TotalOnes - OnesOnLeft)) = Max of (ZerosOnLeft - OnesOnLeft) + TotalOnes (as TotalOnes is constant)
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        zeros,ones = 0,0
        maxval = float('-inf')
        for i in range(len(s)):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            if i != len(s)-1:
                maxval = max(maxval,zeros-ones)
        return maxval+ones