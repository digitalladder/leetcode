#problem 448 / find all numbers disappeared in an array
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            new_index = abs(nums[i])-1      #用数组下标做标记，记录已经出现的数字
            if nums[new_index] > 0:         #如出现数字为3，对应数组下标为3的数乘-1
                nums[new_index] *= -1
        result = []
        for i in range(1,len(nums)+1):
            if nums[i-1] >0:
                result.append(i)
        return result