#problem 445 / add two numbers II
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1
        def add(l1,l2,offset):
            if not l1:
                return None
            carry = 0
            if offset > 0:
                res = add(l1.next,l2,offset-1)
                node = ListNode(l1.val)
            elif offset == 0:
                res = add(l1.next,l2.next,offset)
                node = ListNode(l1.val+l2.val)
            if res and res.val > 9:
                res.val = res.val%10
                carry = 1
            node.val += carry
            node.next = res
            return node
        def size(head):
            if not head:
                return 0
            count = 0
            while head:
                count += 1
                head = head.next
            return count
        size1,size2 = size(l1),size(l2)
        if size1 >= size2:
            result = add(l1,l2,size1-size2)
        else:
            result = add(l2,l1,size2-size1)
        if result.val > 9:
            result.val = result.val%10
            head = ListNode(1)
            head.next = result
            return head
        return result