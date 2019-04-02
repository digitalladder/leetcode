#Problem 47 /Permutations II
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        path=[]
        nums.sort()
        self.dfs(nums,path,result)
        return result
    def dfs(self,nums,path,result):
        if len(path)==len(nums):
            result.append(nums[x] for x in path)
            return
        i=0
        while i<len(nums):
            if i not in path:
                self.dfs(nums,path+[i],result)
                while i+1<len(nums) and nums[i+1]==nums[i]:
                    i=i+1
            i=i+1