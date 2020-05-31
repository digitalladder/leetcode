# problem 1457 / pseudo-palindromic paths in a binary tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.counter = 0
        def dfs(root,temp):
            if not root.left and not root.right:
                if self.ispalindromic(temp+[root.val]):
                    self.counter += 1
                    return
            if root.left:
                dfs(root.left,temp+[root.val])
            if root.right:
                dfs(root.right,temp+[root.val])
        dfs(root,[])
        return self.counter
        
    def ispalindromic(self,path):
        c = collections.Counter(path)
        flag = 0
        for key in c:
            if c[key]%2 != 0 and flag ==  1:
                return False
            elif c[key]%2 != 0 and flag == 0:
                flag = 1
        return True