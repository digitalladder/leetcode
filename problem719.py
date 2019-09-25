#problem 719 / find k-th smallest pair distance
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def count(x):
            total = left = 0
            for right,val in enumerate(nums):
                while val - nums[left] > x:
                    left += 1
                total += right - left
            return total >= k
        nums.sort()
        lo = 0
        hi = nums[-1]-nums[0]
        while lo < hi:
            mid = (lo+hi)//2
            if count(mid):
                hi = mid
            else:
                lo = mid+1
        return lo