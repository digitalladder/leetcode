#problem 146 / LRU cache
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.size = 0
        self.cache = {}
        self.linked_list = dlinklist()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.linked_list.move_tohead(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.linked_list.move_tohead(node)
        else:
            node = Node(key,value)
            self.cache[key] = node
            self.linked_list.add_node_tohead(node)
            self.size += 1
        if self.size > self.cap:
            tail = self.linked_list.pop_tail()
            self.cache.pop(tail.key)
            self.size -= 1
        
class Node(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None
        
class dlinklist(object):
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
    
    def move_tohead(self,node):
        self.remove(node)
        self.add_node_tohead(node)
    
    def add_node_tohead(self,node):
        nextnode = self.head.next
        node.next = nextnode
        nextnode.pre = node
        self.head.next = node
        node.pre = self.head
        
    def pop_tail(self):
        res = self.tail.pre
        self.remove(res)
        return res
    
    def remove(self,node):
        pre = node.pre
        new = node.next
        pre.next = new
        new.pre = pre

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

##利用Ordereddict
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last = False)