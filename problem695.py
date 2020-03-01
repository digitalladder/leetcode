#problem 695 / max area of island
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = collections.deque()
        res = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    grid[i][j] = 0
                    count = 1
                    while queue:
                        r,c = queue.popleft()
                        for nr,nc in {(r,c+1),(r,c-1),(r-1,c),(r+1,c)}:
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                                queue.append((nr,nc))
                                grid[nr][nc] = 0
                                count += 1
                    res = max(res,count)                #放在if语句里是为了处理边界，如 [[0]] ,此时没有创建count，直接返回res处置
        return res