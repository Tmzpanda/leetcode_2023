def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    pred = dummy = ListNode(-1) # dummy node

    while l1 and l2:
        if l1.val <= l2.val:
            pred.next = l1
            l1 = l1.next
        else:
            pred.next = l2
            l2 = l2.next
        pred = pred.next
        
    pred.next = l1 or l2
    
    return dummy.next 
