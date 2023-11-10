# set
def hasCycle(head: Optional[ListNode]) -> bool:
    visited = set()
    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next

    return False

# pointers
def hasCycle(head: Optional[ListNode]) -> bool:
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True
