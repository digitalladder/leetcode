#problem 560 /subarray sum equals k
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presum = {0:1}
        sums = 0
        count = 0
        for i in range(len(nums)):
            sums = sums + nums[i]
            if sums - k in presum:
                count = count+presum[sums-k]
            presum[sums] = presum.get(sums,0)+1
        return count