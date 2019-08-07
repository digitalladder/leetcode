#problem 2 / add two numbers
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = dummy = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            cur = (v1+v2+carry)%10
            carry = (v1+v2+carry)//10       #注意cur和carry计算顺序不能反，cur计算完之后再更新carry
            dummy.next = ListNode(cur)
            dummy = dummy.next
        return head.next