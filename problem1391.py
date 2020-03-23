#problem 1391 / check if there is a valid path in a grid
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        def pos(x,y,street):
            if street == 1:
                return [(x,y-1,(1,4,6)),(x,y+1,(1,3,5))]
            elif street == 2:
                return [(x+1,y,(2,5,6)),(x-1,y,(2,3,4))]
            elif street == 3:
                return [(x+1,y,(2,5,6)),(x,y-1,(1,4,6))]
            elif street == 4:
                return [(x+1,y,(2,5,6)),(x,y+1,(1,3,5))]
            elif street == 5:
                return [(x-1,y,(2,3,4)),(x,y-1,(1,4,6))]
            else:
                return [(x-1,y,(2,3,4)),(x,y+1,(1,3,5))]
            
        n = len(grid)
        m = len(grid[0])
        stack = [(0,0,grid[0][0])]
        visited = set()
        while stack:
            p = stack.pop()
            x,y = p[0],p[1]
            street = grid[x][y]
            if (x,y) == (n-1,m-1):
                return True
            if (x,y) not in visited:
                visited.add((x,y))
                position = pos(x,y,street)
                for px,py,pstreet in position:
                    if 0<=px<n and 0<=py<m and (grid[px][py] in pstreet):
                        stack.append((px,py))
        return False
        