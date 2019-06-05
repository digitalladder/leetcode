#problem 146 / LRU cache
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1
        self.move_to_head(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.cache.get(key)
        if not node:
            newnode = DoubleLinkedNode()
            newnode.key = key
            newnode.val = value
            
            self.cache[key] = newnode
            self.add_node(newnode)
            self.size = self.size+1
            
            if self.size > self.capacity:
                tail = self.remove_tail()
                del self.cache[tail.key]
                self.size = self.size-1
        else:
            node.val = value
            self.move_to_head(node)
        
    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def remove_tail(self):
        rmnode = self.tail.prev
        rmnode.prev.next = self.tail
        self.tail.prev = rmnode.prev
        return rmnode
        
    def move_to_head(self, node):
        mn = node
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        
class DoubleLinkedNode():
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)