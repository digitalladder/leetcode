#problem 1102 / path with maximuum minimum value
class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        m = len(A[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        maxheap = [(-A[0][0],0,0)]
        while maxheap:
            val,x,y = heapq.heappop(maxheap)
            if x == n-1 and y == m-1:
                return -val
            for nx,ny in {(x+1,y),(x-1,y),(x,y+1),(x,y-1)}:
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    heapq.heappush(maxheap,(max(val,-A[nx][ny]),nx,ny))
        return -1
            