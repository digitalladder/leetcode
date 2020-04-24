#problem 143 / reorder list
# linked list / list merge / double pointer

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev,curr = None,slow
        while curr:
            curr.next,prev,curr = prev,curr,curr.next
        
        first,second = head,prev
        print(first.val,second.val)
        while second.next:
            first.next,first = second,first.next
            second.next,second = first,second.next