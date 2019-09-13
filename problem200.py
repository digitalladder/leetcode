#problem 200 / number of islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid),len(grid[0])
        count = 0
        def bfs(i, j):
            q, grid[i][j] = [(i, j)], "0"
            for i, j in q:
                for x, y in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                        grid[x][y] = "0"
                        q.append((x, y))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i,j)
                    count += 1
        return count

#
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        neighbor = []
        m, n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '0'
                    neighbor.append((i,j))
                    for i,j in neighbor:
                        for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                                neighbor.append((x,y))
                                grid[x][y] = '0'
        return count