# problem 1437 / check if all 1's are at least length k places away
# array
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        counter = k
        for i in range(len(nums)):
            if nums[i] == 1:
                if counter < k:
                    return False
                counter = 0
            else:
                counter += 1
        return True