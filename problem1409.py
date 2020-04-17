#problem 1409 / Queries on a Permutation With Key
class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        pre = head = Node(0)
        for i in range(1,m+1):
            pre.next = Node(i)
            pre = pre.next
        res = []
        for query in queries:
            start = head.next
            pre = head
            i = 0
            while True:
                if start.value == query:
                    res.append(i)
                    if i != 0:
                        pre.next = start.next
                        start.next = head.next
                        head.next = start
                    break
                else:
                    start = start.next
                    pre = pre.next
                    i += 1
        return res
            
class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None