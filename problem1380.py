#problem 1380 / lucky numbers in a matrix
class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        minimum = [float('inf')]*len(matrix)
        maximum = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
                minimum[i] = min(minimum[i],matrix[i][k])
                maximum[k] = max(maximum[k],matrix[i][k])
        res = []
        for m in minimum:
            if m in maximum:
                res.append(m)
        return res