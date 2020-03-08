#problem 1377 / frog position after t seconds
class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        tree = collections.defaultdict(set)
        for edge in edges:
            tree[edge[0]].add(edge[1])
            tree[edge[1]].add(edge[0])
        queue = collections.deque([(1,0,1)])
        visited = set()
        while queue:
            vertex,time,prob = queue.popleft()
            visited.add(vertex)
            if vertex == target and time == t:
                return 1.0/prob
            if vertex == target and time < t:
                if not tree[vertex]-visited:
                    return 1.0/prob
                return 0
            if time > t:
                continue
            n = tree[vertex]-visited
            n = max(len(n),1)
            for v in tree[vertex]:
                if v not in visited:
                    queue.append((v,time+1,prob*n))
        return 0