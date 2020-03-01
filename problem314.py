#problem 314 / binary tree vertical order traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        col = collections.defaultdict(list)
        queue = collections.deque([(root,0)])       #必须是 [()] 必须要有方括号
        while queue:
            node,i = queue.popleft()
            if node:
                col[i].append(node.val)
                queue.append((node.left,i-1))
                queue.append((node.right,i+1))
        return [col[l] for l in sorted(col)]        #defaultdict 可排序，返回排序后的所有key