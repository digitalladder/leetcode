#problem 463 / island perimeter
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        raw = len(grid)     #len()运算会影响速度，最好只在开头运算一次
        col = len(grid[0])
        for i in range(raw):
            for j in range(col):
                if grid[i][j] == 1:
                    res += 4
                    if i+1 < raw and grid[i+1][j] == 1:
                        res -= 2
                    if j+1 < col and grid[i][j+1] == 1:
                        res -= 2
        return res