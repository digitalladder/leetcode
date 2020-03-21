#problem 106 / construct binary tree from inorder and postorder
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            val = postorder.pop()
            idx = inorder.index(val)
            root = TreeNode(val)
            root.right = self.buildTree(inorder[idx+1:],postorder)
            root.left = self.buildTree(inorder[:idx],postorder)
            return root

# 无需 取index操作， O（n）复杂度
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build(bound = None):
            if not inorder or inorder[-1] == bound: return None
            root = TreeNode(postorder.pop())
            root.right = build(root.val)    #root作为遍历inorder时结束的位置
            inorder.pop()
            root.left = build(bound)        #上一层的结束为止
            return root

        return build()