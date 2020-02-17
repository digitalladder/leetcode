#problem 572 / subtree of another tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        def checkequal(s,t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and checkequal(s.left,t.left) and checkequal(s.right,t.right)
            
        def traverse(s,t):
            if not s:
                return False
            if s.val == t.val and checkequal(s,t):
                return True
            return traverse(s.left,t) or traverse(s.right,t)
        return traverse(s,t)