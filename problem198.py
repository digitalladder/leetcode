#problem 198 / house robber
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        premax = 0
        curmax = 0
        for n in nums:
            temp = curmax
            curmax = max(premax+n,curmax)
            premax = temp
        return curmax