#problem 114 / flatten binary tree to linked list
#最简洁的方法
class Solution(object):
    list_head = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root:
            self.flatten(root.right)
            self.flatten(root.left)
            root.left = None
            root.right = self.list_head
            
            self.list_head = root

#方法2
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        right = self.flatten(root.right)
        left = self.flatten(root.left)
        
        root.left = None
        
        if left:
            root.right = left
            while left.right:
                left = left.right
            left.right = right
        else:
            root.right = right
        
        return root
            