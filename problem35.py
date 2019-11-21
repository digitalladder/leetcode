# problem 35 / search insert position
##二分法
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[-1]:
            return len(nums)
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mid = lo+(hi-lo)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid+1
            else:
                hi = mid
        return lo

##一次循环
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif nums[i]>target:
                return i
        else:
            return len(nums)