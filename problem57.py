#problem 57 /Maxmium Subarray
class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return
        temp = nums[0]
        maxv = nums[0]
        for i in range(1,len(nums)):
            temp = max(nums[i], temp+nums[i])
            maxv = max(temp,maxv)
        return maxv