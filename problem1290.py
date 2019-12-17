#problem 1290 / convert binary number in a linked list to integer
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = 0
        while head:
            res *= 2
            res += head.val
            head = head.next
        return res