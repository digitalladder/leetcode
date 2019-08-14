#problem 138 / copy list with random pointer

# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        dummy = head
        while dummy:
            temp = Node(dummy.val,dummy.next,None)
            dummy.next = temp
            dummy = dummy.next.next
        dummy = head
        while dummy:
            if dummy.random:
                dummy.next.random = dummy.random.next
            else:
                dummy.next.random = None
            dummy = dummy.next.next
        oldlist = head
        newlist = head.next
        newhead = head.next
        while oldlist:
            oldlist.next = oldlist.next.next
            newlist.next = newlist.next.next if newlist.next else None
            oldlist = oldlist.next
            newlist = newlist.next
        return newhead