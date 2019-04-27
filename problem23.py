#problem 23 /merge k sorted lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0,amount-interval,interval*2):
                lists[i] = self.merge2lists(lists[i],lists[i+interval])
            interval = interval*2
        return lists[0]
        
    def merge2lists(self,l1,l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next