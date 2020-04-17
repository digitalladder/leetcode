#problem 653 / two sum IV input is a BST
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        arr = self.inorder(root)
        l = 0
        r = len(arr)-1
        while l < r:
            sumval = arr[l]+arr[r]
            if sumval == k:
                return True
            if sumval < k:
                l += 1
            else:
                r -= 1
        return False
        
    def inorder(self,root):
        if not root:
            return []
        return self.inorder(root.left)+[root.val]+self.inorder(root.right)