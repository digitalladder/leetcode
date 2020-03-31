#problem 229 / majority element II
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        el1,el2 = 0,0
        counter1,counter2 = 0,0
        for num in nums:
            if num == el1:
                counter1 += 1
            elif num == el2:
                counter2 += 1
            elif counter1 == 0:
                el1 = num
                counter1 = 1
            elif counter2 == 0:
                el2 = num
                counter2 = 1
            else:
                counter1 -= 1
                counter2 -= 1
        counter1,counter2 = 0,0
        for num in nums:
            if num == el1:
                counter1 += 1
            elif num == el2:
                counter2 += 1
        res = []
        if counter1 > len(nums)/3:
            res.append(el1)
        if counter2 > len(nums)/3:
            res.append(el2)
        return res