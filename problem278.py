#problem 278 / first bad version
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end:
            mid = start+(end-start)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid+1
        return start