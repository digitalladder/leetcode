#problem 986 / interval list intersections
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        i, j = 0,0
        while i < len(A) and j < len(B):
            lo = max(A[i][0],B[j][0])
            hi = min(A[i][1],B[j][1])
            if lo <= hi:
                ans.append([lo,hi])
            if A[i][1] >= B[j][1]:
                j += 1
            else:
                i += 1
        return ans