#problem 814 / binary tree pruning 剪枝
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def prune(node):
            if not node:
                return
            node.left = prune(node.left)
            node.right = prune(node.right)
            if not node.left and not node.right and node.val == 0:
                return
            return node         #注意递归返回值
        return prune(root)