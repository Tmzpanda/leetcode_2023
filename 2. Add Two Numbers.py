def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    pred = dummy = ListNode(-1)
        
    carry = 0 
    while l1 or l2 or carry:
        num = 0 
        if l1:
            num += l1.val 
            l1 = l1.next
        if l2:
            num += l2.val 
            l2 = l2.next
        num += carry
        digit, carry = num % 10, num // 10
        node = ListNode(digit)
        
        pred.next = node 
        pred = node

    return dummy.next
    
