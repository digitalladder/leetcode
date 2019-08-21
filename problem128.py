#problem 128 / longest consecutive sequence
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        numset = set(nums)
        for num in numset:
            if num-1 not in numset:
                current = num
                currentlength = 1
                while current+1 in numset:
                    current += 1
                    currentlength += 1
                longest = max(longest,currentlength)
        return longest