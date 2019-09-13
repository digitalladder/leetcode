#problem 105 / construct binary tree from preorder and inorder
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pre_idx = 0
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        def helper(in_left = 0, in_right = len(inorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None
            
            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion 
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root
        return helper()

##简洁写法，直接截取inorder作为传入参数
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            idx = inorder.index(root_val)
            root.left = self.buildTree(preorder,inorder[:idx])
            root.right = self.buildTree(preorder,inorder[idx+1:])
            return root

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None