#problem 41 / first missing positive
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 not in nums:
            return 1
        n = len(nums)
        if n == 1:
            return 2
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        for i in range(n):
            number = abs(nums[i])
            if number == n:
                nums[0] = - abs(nums[0])
            else:
                nums[number] = - abs(nums[number])
        for i in range(1,n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n+1