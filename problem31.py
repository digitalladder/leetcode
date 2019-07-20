#problem 31 / next permutation
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last = len(nums)-1
        while last-1 >= 0 and nums[last] <= nums[last-1]:
            last -= 1
        i = last
        if last-1 >= 0:
            while i < len(nums) and nums[i] > nums[last-1]:
                i += 1
            #print(last)
            #print(i)
            nums[last-1],nums[i-1] = nums[i-1],nums[last-1]
        self.reverse(nums,last)
            
    def reverse(self,nums,start):
        end = len(nums)-1
        while end > start:
            nums[start],nums[end] = nums[end],nums[start]
            start = start+1
            end = end-1