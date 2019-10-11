#problem 1218 / longest arithmetic subsequence of given difference
class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        count = {}
        for a in arr:
            count[a] = 1+count.get((a-difference),0)
        return max(count.values())