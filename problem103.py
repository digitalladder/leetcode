#problem 103 / binary tree zigzag level order traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root
        reverse = -1
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if reverse == 1:
                temp.reverse()
            res.append(temp)
            reverse = -1*reverse
        return res