#problem 34 / find first and last position of element in sorted array
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftidx = self.binarysearch(nums,target,True)
        if leftidx == len(nums) or nums[leftidx] != target:
            return [-1,-1]
        return [leftidx,self.binarysearch(nums,target,False)-1]
        
    def binarysearch(self,nums,target,ifleft):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo+hi)/2
            if nums[mid] > target or (ifleft and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1
        return lo