#problem 1382 / balance a binary search tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(root):
            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                treearr.append(root.val)
                root = root.right
        def rebuild(start,end):
            if start > end:
                return None
            mid = (start+end)/2
            root = TreeNode(treearr[mid])
            root.left = rebuild(start,mid-1)
            root.right = rebuild(mid+1,end)
            return root
        treearr = []
        inorder(root)
        root = rebuild(0,len(treearr)-1)
        return root