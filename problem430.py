#problem 430 / flatten a multilevel doubly linked list
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        dummy = Node(None,None,head,None)
        self.dfs(dummy,head)
        dummy.next.prev = None
        return dummy.next
        
    def dfs(self,pre,cur):
        if not cur:
            return pre
        nextnode = cur.next
        cur.prev = pre
        pre.next = cur
        tail = self.dfs(cur,cur.child)
        cur.child = None
        return self.dfs(tail,nextnode)