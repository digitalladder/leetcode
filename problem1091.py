#problem 1091 / shortest path in binary matrix
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or grid[0][0] == 1:
            return -1
        queue = collections.deque()
        visited = set()
        n = len(grid)
        queue.append([0,0,1])
        while queue:
            x,y,count = queue.popleft()
            if x == n-1 and y == n-1:
                return count
            for nx,ny in {(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)}:
                if 0<=nx<n and 0<=ny<n and grid[nx][ny] == 0 and (nx,ny) not in visited:
                    queue.append([nx,ny,count+1])
                    visited.add((nx,ny))
        return -1