#problem 490 / the maze
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        n = len(maze)
        m = len(maze[0])
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = collections.deque([start])
        visited = set()
        visited.add((start[0],start[1]))
        while queue:
            x,y = queue.popleft()
            if [x,y] == destination:
                return True
            for i in range(4):
                nx,ny = x+direction[i][0],y+direction[i][1]
                while 0<=nx<n and 0<=ny<m and maze[nx][ny] == 0:
                    nx += direction[i][0]
                    ny += direction[i][1]
                if (nx-direction[i][0],ny-direction[i][1]) not in visited:
                    queue.append([nx-direction[i][0],ny-direction[i][1]])
                    visited.add((nx-direction[i][0],ny-direction[i][1]))
        return False
                