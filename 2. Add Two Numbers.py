def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    tail = dummy
    
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
        
        tail.next = node 
        tail = node

    return dummy.next
