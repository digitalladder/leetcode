#problem 297 / serialize and deserialize binary tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res.append(str(node.val))
            else:
                res.append('None')
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        ls = data.split(',')
        queue = collections.deque()
        idx = 1
        root = TreeNode(int(ls[0]))
        queue.append(root)
        while queue and idx < len(ls):
            node = queue.popleft()
            if ls[idx] != 'None':
                left = TreeNode(int(ls[idx]))
                node.left = left
                queue.append(left)
            idx += 1
            if ls[idx] != 'None':
                right = TreeNode(int(ls[idx]))
                node.right = right
                queue.append(right)
            idx += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))