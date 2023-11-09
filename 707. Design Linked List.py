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
        
        prev = self.head
        for _ in range(index):
            prev = prev.next

        node = ListNode(val)
        node.next = prev.next
        prev.next = node

        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.count:
            return
        
        prev = self.head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next

        self.count -= 1


# DoubleLinkedList

