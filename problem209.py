#problem 209 / minimum size subarray sum
# two pointer
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = float('inf')
        left = 0
        sumval = 0
        for i in range(len(nums)):
            sumval += nums[i]
            while sumval >= s:
                res = min(res,i-left+1)
                sumval -= nums[left]
                left += 1
        if res < float('inf'):
            return res
        else:
            return 0
