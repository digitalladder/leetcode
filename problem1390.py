#problem 1390 / four divisors
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            temp = {1,num}
            for i in range(2,int(sqrt(num))+1):
                if num%i == 0:
                    temp.add(i)
                    temp.add(num/i)
                if len(temp) > 4:
                    temp = []
                    break
            if len(temp) == 4:
                for t in temp:
                    res += t
        return res