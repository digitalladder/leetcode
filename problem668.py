#problem 668 / kth smallest number in multiplication table
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def enough(x):
            count = 0
            for i in range(1,m+1):
                count += min(x//i,n)
            return count >= k
        if k > m*n:
            return False
        lo = 1
        hi = m*n
        while lo < hi:
            mid = (lo+hi)//2
            if enough(mid):
                hi = mid
            else:
                lo = mid+1
        return lo