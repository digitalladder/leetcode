#problem 1036 / escape a large maze
class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        def bfs(blocked,source,target):
            n = 10**6
            level = 0
            visited = set()
            queue = collections.deque([(source[0],source[1])])
            while queue:
                for i in range(len(queue)):         #一层一层的遍历，所以要加for循环
                    sx,sy = queue.popleft()
                    for nx,ny in {(sx-1,sy),(sx+1,sy),(sx,sy-1),(sx,sy+1)}:
                        if [nx,ny] == target:
                            return True
                        if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited and (nx,ny) not in blocked:
                            queue.append((nx,ny))
                            visited.add((nx,ny))
                level += 1
                if level >= len(blocked)*2:         #worst case 需要 len（）*2 层
                    return True
            else:
                return False
        blocked = set(map(tuple,blocked))
        return bfs(blocked,source,target) and bfs(blocked,target,source)

"""
4   5   6   7   8   *
3   4   5   6   *
2   3   4   *
1   2   *
s   *       t
*

this is an example of worst case
s is source, * is blocked, t is target, need at least 2*len(blocked) levels bfs to make sure s can escape blocks
"""