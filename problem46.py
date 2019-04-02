#Problem 46 /Permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        permutation=[]
        self.dfs(nums,permutation,result)
        return result
    def dfs(self,nums,permutation,result):
        if len(nums) == 1:
            result.append(permutation+nums)
            return
        for i, n in enumerate(nums):
            permutation.append(n)
            self.dfs(nums[:i]+nums[i+1:],permutation,result)
            permutation.pop()