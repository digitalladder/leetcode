#problem 215 / Kth largest element in an array
#快排算法应用，将数组分为两部分知道大于pivot的数个数为k
#kth largest转换为 n-k smallest
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < k:
            return
        start = 0
        end = len(nums)-1
        while start <= end:
            temp = self.partition(nums,start,end)
            if temp == len(nums)-k:
                return nums[temp]
            if temp > len(nums)-k:
                end = temp-1
            if temp < len(nums)-k:
                start = temp+1
        
    def partition(self,nums,start,end):
        pivot = random.randint(start,end)
        nums[pivot],nums[start] = nums[start],nums[pivot]
        pivot = start
        while start < end:
            while nums[end] > nums[pivot] and end > start:
                end -= 1
            while nums[start] <= nums[pivot] and end > start:
                start += 1
            nums[start],nums[end] = nums[end],nums[start]
        nums[pivot],nums[start] = nums[start],nums[pivot]
        return start
                