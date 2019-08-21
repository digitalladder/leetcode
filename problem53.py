#problem 53 / maximum subarry
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float('-inf')
        currentsum = 0
        for i in range(len(nums)):
            currentsum += nums[i]
            res = max(currentsum,res)
            if currentsum < 0:
                currentsum = 0
        return res