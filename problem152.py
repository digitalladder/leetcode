#problem 152 / maximum product subarray
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        imax = imin = res
        for i in range(1,len(nums)):
            if nums[i] < 0:
                imax,imin = imin,imax
            imax = max(nums[i],imax*nums[i])
            imin = min(nums[i],imin*nums[i])
            res = max(res,imax)
        return res