#problem 907 / sum of subarray minimums
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        s = []
        A = [0] + A + [0]               #通过收尾加零处理边界条件，尾部的零使最后递增的序列可以弹出栈
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % (10**9 + 7)

#不使用收尾加零，需要处理栈内剩余数据
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1] if s else -1
                res += A[j]*(i-j)*(j-k)
            s.append(i)
        while s:
            j = s.pop()
            k = s[-1] if s else -1
            res += A[j]*(len(A)-j)*(j-k)
        return res%(10**9+7)