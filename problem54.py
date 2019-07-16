#problem 54 / spiral matrix
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])
        res = []
        start = 0
        while col > start*2 and row > start*2:
            self.printincircle(matrix,col,row,start,res)
            start = start+1
        return res
    
    def printincircle(self,matrix,col,row,start,res):
        endx = col-1-start
        endy = row-1-start
        
        for i in range(start,endx+1):
            res.append(matrix[start][i])
        
        if endy > start:
            for i in range(start+1,endy+1):
                res.append(matrix[i][endx])
                
        if endx > start and endy > start:
            for i in range(endx-1, start-1,-1):
                res.append(matrix[endy][i])
        if endy-1 > start and endx > start:
            for i in range(endy-1,start,-1):
                res.append(matrix[i][start])

# 用生成器 代码更简洁
class Solution(object):
    def spiralOrder(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans