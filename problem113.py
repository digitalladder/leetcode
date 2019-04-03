#problem 113 /Path ssum II
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path,result = [],[]
        self.dfs(root,path,result,sum)
        return result
    def dfs(self,root,path,result,sum):
        if not root:
            return
        if not root.left and not root.right and root.val == sum:
            result.append(path+[root.val])
        if root.left:
            path.append(root.val)
            self.dfs(root.left,path,result,sum-root.val)
            path.pop()
        if root.right:
            path.append(root.val)
            self.dfs(root.right,path,result,sum-root.val)
            path.pop()