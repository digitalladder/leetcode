#problem 1248 / count number of nice subarrays
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dic = {0:0}
        count = 1
        res = 0
        for i in range(n):
            if nums[i]%2 == 1:
                dic[count] = i+1
                count += 1
        if len(dic)-1 < k:
            return 0
        for j in range(k,len(dic)):
            if j+1 < len(dic):
                res += (dic[j-k+1]-dic[j-k])*(dic[j+1]-dic[j])
            else:
                res += (dic[j-k+1]-dic[j-k])*(n+1-dic[j])
        return res