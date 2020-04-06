#problem 137 / single number II
# bit manipulate
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        apper_once = apper_twice = 0
        for num in nums:
            apper_once = ~apper_twice&(apper_once^num)
            apper_twice = ~apper_once&(apper_twice^num)
        return apper_once