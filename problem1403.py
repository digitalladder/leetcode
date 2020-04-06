#problem 1403 / minimum subsequence in non-increasing order
class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = sum(nums)
        nums.sort(reverse = 1)
        sumval = 0
        res = []
        for num in nums:
            sumval += num
            res.append(num)
            if sumval > total-sumval:
                return res
        