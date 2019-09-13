#problem 117 / populating next right pointers in each node II
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
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
        temp = dummytemp = Node(0)
        dummy = root
        while root:
            temp.next = root.left
            if temp.next:
                temp = temp.next
            temp.next = root.right
            if temp.next:
                temp = temp.next
            root = root.next
            if not root:
                root = dummytemp.next
                temp = dummytemp
        return dummy

#
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        queue = [root]
        level = []
        while queue:
            p = queue.pop(0)
            if p.left:
                level.append(p.left)
            if p.right:
                level.append(p.right)
            if queue:
                p.next = queue[0]
            else:
                p.next = None
            if not queue and level:
                queue = level
                level = []
        return root