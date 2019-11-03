#problem 133 / clone graph
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        d = {}
        def deepcopy(node):
            copynode = Node(node.val,[])
            d[node] = copynode
            for n in node.neighbors:
                if n not in d:
                    copynode.neighbors.append(deepcopy(n))
                else:
                    copynode.neighbors.append(d[n])
            return copynode
        return deepcopy(node)

##iterate
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        copynode = Node(node.val,[])
        queue = collections.deque()
        queue.append(node)
        d = {node:copynode}
        while queue:
            node = queue.popleft()
            for n in node.neighbors:
                if n not in d:                                  #注意 if 语句下需要执行的操作
                    copyneighbor = Node(n.val,[])
                    d[n] = copyneighbor
                    d[node].neighbors.append(copyneighbor)
                    queue.append(n)
                else:
                    d[node].neighbors.append(d[n])
        return copynode