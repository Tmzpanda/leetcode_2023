class ListNode:  # single linked list node
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.count = 0
        
    def append(self, value: int) -> bool:
        node = ListNode(value)
        if self.count == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1

    def popleft(self) -> bool:
        if self.count == 0:
            raise IndexError("Queue is empty")

        value = self.head.value
        self.head = self.head.next
        self.count -= 1
        return value
      
