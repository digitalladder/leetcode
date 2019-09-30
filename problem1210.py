#problem 1210 / minimum moves to reach target with rotations
class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s,t,v,moves,n = [(0,0,'h')],[],set(),0,len(grid)
        while s:
            for i in s:
                if i in v:
                    continue
                if i == (n-1,n-2,'h'):
                    return moves
                (a,b,c),_ = i,v.add(i)
                
                if c == 'h':
                    if b+2 < n and grid[a][b+2] == 0:
                        t.append((a,b+1,'h'))
                    if a+1 < n and grid[a+1][b] == 0 and grid[a+1][b+1] == 0:
                        t.append((a,b,'v'))
                        t.append((a+1,b,'h'))
                elif c == 'v':
                    if a+2 < n and grid[a+2][b] == 0:
                        t.append((a+1,b,'v'))
                    if b+1 < n and grid[a][b+1] == 0 and grid[a+1][b+1] == 0:
                        t.append((a,b+1,'v'))
                        t.append((a,b,'h'))
            moves += 1
            s = t
            t = []
        return -1
                