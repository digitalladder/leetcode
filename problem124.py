#problem 124 / binary tree maximum path sum
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_gain(node):
            if not node:
                return 0

            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain
            
            # update max_sum if it's better to start a new path
            max_gain.max_sum = max(max_gain.max_sum, price_newpath)
            #使用函数属性来修改max_sum值，不能直接传入变量修改，数字属于不可变对象。也可以用global变量。python3中可用nonlocal
        
            # for recursion :
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)
        
        max_gain.max_sum = float('-inf')
        max_gain(root)
        return max_gain.max_sum

#python3 nonlocal方法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)
            return node.val + max(left_gain, right_gain)      
        max_sum = float('-inf')
        max_gain(root)
        return max_sum