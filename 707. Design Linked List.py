# Single LinkedList
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1) # sentinel node as pseudo-head
        # self.tail = None
        self.count = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.count:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.count, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return
        if index < 0:
            index = 0
        
        pred = self.head
        for _ in range(index):
            pred = pred.next

        node = ListNode(val)
        node.next = pred.next
        pred.next = node

        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.count:
            return
        
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next

        self.count -= 1

# DoubleLinkedList
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.count:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next

        return curr.val
        
    def addAtHead(self, val: int) -> None:
        pred, succ = self.head, self.head.next
        node = ListNode(val)

        node.prev = pred
        node.next = succ
        pred.next = node
        succ.prev = node
        self.count += 1
        
    def addAtTail(self, val: int) -> None:
        pred, succ = self.tail.prev, self.tail
        node = ListNode(val)

        node.prev = pred
        node.next = succ
        pred.next = node
        succ.prev = node
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return
        if index < 0:
            index = 0

        pred = self.head
        for _ in range(index):
            pred = pred.next
        succ = pred.next

        node = ListNode(val)
        pred.next = node
        succ.prev = node
        node.prev = pred
        node.next = succ

        self.count += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.count:
            return

        pred = self.head
        for _ in range(index):
            pred = pred.next
        succ = pred.next.next

        pred.next = succ
        succ.prev = pred

        self.count -= 1
