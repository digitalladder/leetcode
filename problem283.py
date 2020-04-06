#problem 283 / move zeroes
# two pointers
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] != 0:
                i += 1
            else:
                for j in range(i+1,len(nums)):
                    if nums[j] != 0:
                        nums[i],nums[j] = nums[j],nums[i]
                        i += 1
                        break
                else:
                    break
        return nums