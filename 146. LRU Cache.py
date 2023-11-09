# OrderedDict
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  # cache

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key, last=True) # move to the end
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # pop from the beginning

          
# DoubleLinkedList + lookup
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}  
        self.head = ListNode(-1, -1)    # sentinel node as pseudo-head
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        node = self.lookup[key]
        self.remove(node)   # move to the end
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            old_node = self.lookup[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.lookup[key] = node
        self.add(node)

        if len(self.lookup) > self.capacity:
            node_to_delete = self.head.next  # pop from the beginning
            self.remove(node_to_delete)
            del self.lookup[node_to_delete.key]

    def add(self, node):
        pred, succ = self.tail.prev, self.tail
        pred.next = node
        node.prev = pred
        node.next = succ
        succ.prev = node

    def remove(self, node):
        pred, succ = node.prev, node.next
        pred.next = succ
        succ.prev = pred
