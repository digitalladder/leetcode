#problem 1130 / minimum cost tree from leaf values
# n^2 solution
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        n = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i - 1:i]+arr[i + 1:i+2]) * arr.pop(i)        #字符串截取不会产生下标越界
            #如果 i 为list最后一个元素，arr[i+1]会下标越界，但 arr[i+1:i+2] 不会，只会返回空list 【】
        return res

#利用stack 一次循环
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = [float('inf')]
        res = 0
        for a in arr:
            while stack[-1] <= a:
                temp = stack.pop()
                res += temp*min(stack[-1],a)
            stack.append(a)
        while len(stack) > 2:
            temp = stack.pop()
            res += temp*stack[-1]
        return res