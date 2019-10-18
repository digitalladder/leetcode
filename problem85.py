#problem 85 / maximal rectangle
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        left = [0]*n
        right = [n]*n
        height = [0]*n
        maxarea = 0
        for i in range(m):
            cur_left,cur_right = 0,n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j],cur_left)     #与上一行的相比较
                else:
                    height[j] = 0
                    left[j] = 0
                    cur_left = j+1
            for j in range(n-1,-1,-1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j],cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                maxarea = max(maxarea,height[j]*(right[j]-left[j]))
        return maxarea

#方法2： 遍历每一行，转换为直方图，利用stack求最大矩形面积（84题方法）