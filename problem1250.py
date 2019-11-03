#problem 1250 / check if it is a good array

# If a % x = 0 and b % x = 0,
# appareantly we have (pa + qb) % x == 0
# If x > 1, making it impossible pa + qb = 1.
# Just check if all the numbers greatest common divisor is 1

class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        gcd = nums[0]
        for a in nums:
            while a:
                gcd, a = a, gcd % a
        return gcd == 1