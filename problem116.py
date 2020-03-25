#problem 116 / populating next right pointers in each node
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)       #这一步相当重要，一定要在开始循环前确定size，否则会出错，因为queue长度是变化的
            for i in range(size):
                node = queue.popleft()
                if i < size-1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root