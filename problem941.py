#problem 941 / valid mountain array
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n < 3:
            return False
        i = 0
        while i+1 < n and A[i] < A[i+1]:
            i += 1
        if i == 0 or i == n-1:
            return False
        while i+1 < n and A[i] > A[i+1]:
            i += 1
        if i < n-1:
            return False
        return True