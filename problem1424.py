#problem 1424 / diagonal traverse II
# array
# 第一行拆散，逐行添加元素， 也可以先求对角层数，再按层扫描
class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        temp = []
        for num in nums[0]:
            temp.append([num])
        
        for i in range(1,n):
            for j,num in enumerate(nums[i]):
                if j+i < len(temp):
                    temp[j+i].insert(0,num)
                else:
                    temp.append([num])
        res = []
        for t in temp:
            res.extend(t)
        return res
# 相同思路，代码更简练
class Solution(object):
    def findDiagonalOrder(self, A):
        res = []
        for i, r in enumerate(A):
            for j, a in enumerate(r):
                if len(res) <= i + j:
                    res.append([])
                res[i + j].append(a)
        return [a for r in res for a in reversed(r)] 