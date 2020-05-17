#problem 16 / 3 sum closest
# two pointer
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        diff = float('inf')
        for i in range(n):
            l,r = i+1,n-1
            while l<r:
                sumval = nums[i]+nums[l]+nums[r]
                if abs(target-sumval)<abs(diff):
                    diff = target-sumval
                if sumval < target:
                    l += 1
                else:
                    r -= 1
            if diff == 0 or target <= nums[i]:
                break
        return target-diff