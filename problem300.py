#problem 300 / longest increasing subsequence
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

##binary search         dp数组按顺序保存可能的最大子序列，不断更新
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        res = 0
        for num in nums:
            i = bisect.bisect_left(dp,num,0,res)
            dp[i] = num
            if i == res:
                res += 1
        return res