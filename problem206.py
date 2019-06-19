#problem 206 /Reverse Linked List
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None
        while cur:
            nextemp = cur.next
            cur.next = prev
            prev = cur
            cur = nextemp
        return prev