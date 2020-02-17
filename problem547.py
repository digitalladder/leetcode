#problem 547 / friend circles
##dfs
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        visited = [0]*n
        count = 0
        def dfs(i):
            for j in range(n):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(j)
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                count += 1
        return count

##bfs
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        queue = collections.deque()
        count = 0
        n = len(M)
        visited = [0]*n
        for i in range(n):
            if visited[i] == 0:
                queue.append(i)
                while queue:
                    s = queue.popleft()
                    visited[s] = 1
                    for j in range(n):
                        if M[s][j] == 1 and visited[j] == 0:
                            queue.append(j)
                count += 1
        return count