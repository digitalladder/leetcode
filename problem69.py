#problem 69 / sqrt(x)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo = 0
        hi = x
        while lo < hi:
            mid = lo+(hi-lo+1)/2        #用右中位数，因为 hi 缩小的时候可以排除 mid，右中位数可以保证不死循环
            if mid*mid > x:             #如果 lo 排除 mid 的时候，就用左中位数
                hi = mid-1
            else:
                lo = mid
        return lo