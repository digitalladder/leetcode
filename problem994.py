#problem 994 / rotting oranges
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        queue = collections.deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
        depth = 0
        while queue:
            r,c,depth = queue.popleft()
            for nr,nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                if 0 <= nr < row and 0 <= nc < col:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc,depth+1))
        if any(1 in row for row in grid):
            return -1
        return depth