#problem 1277 / count square submatrices with all ones
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
                if matrix[i][k] == 0:
                    continue
                if i == 0 or k == 0:
                    res += 1
                else:
                    matrix[i][k] = min(matrix[i-1][k-1],matrix[i][k-1],matrix[i-1][k])+1
                    res += matrix[i][k]
        return res