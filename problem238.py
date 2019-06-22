#problem 238 /Product of Array Except Self
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [0]*n
        output[0] = 1
        for i in range(1,n):
            output[i] = output[i-1]*nums[i-1]
        temp = 1
        for i in reversed(range(n)):
            output[i] = output[i]*temp
            temp = temp*nums[i]
        return output