#problem 98 / validate binary search tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isvalid(root,float('-inf'),float('inf'))
    
    def isvalid(self,root,lowlimit,uplimit):
        if not root:
            return True
        val = root.val
        if val <= lowlimit or val >= uplimit:
            return False
        if not self.isvalid(root.left,lowlimit,val):
            return False
        if not self.isvalid(root.right,val,uplimit):
            return False
        return True

#inorder traverse
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True