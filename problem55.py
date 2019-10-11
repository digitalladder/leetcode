#problem 55 / jump game
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        maxjump = 0
        for i in range(n):
            if maxjump < i:
                return False
            maxjump = max(maxjump,i+nums[i])
        return maxjump >= n-1