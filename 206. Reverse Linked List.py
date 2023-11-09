def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    pred = None
    curr = head
    while curr:
        succ = curr.next
        curr.next = pred

        pred = curr
        curr = succ

    return pred
