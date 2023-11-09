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
    sp = head
    fp = head.next
    while sp != fp:
        if fp is None or fp.next is None:
            return False
        sp = sp.next
        fp = fp.next.next

    return True
