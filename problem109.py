#problem 109 / convert sorted list to binary search tree
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        covertarr = []
        while head:
            covertarr.append(head.val)
            head = head.next
        def helper(lo,hi):
            if lo > hi:
                return None
            mid = (lo+hi)//2
            node = TreeNode(covertarr[mid])
            if lo == hi:
                return node
            node.left = helper(lo,mid-1)
            node.right = helper(mid+1,hi)
            return node
        return helper(0,len(covertarr)-1)