def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    visitedA = set()
    while headA is not None:
        visitedA.add(headA)
        headA = headA.next

    while headB is not None:
        if headB in visitedA:
            return headB
        headB = headB.next

    return None

# two pointers
def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    # When a pointer reaches the end of its linked list, it is redirected to the head of the other linked list. 
    # This way, if there is an intersection point, both pointers will eventually meet at that point.
    p1, p2 = headA, headB
    while p1 != p2:
        if p1 is None:
            p1 = headB
        else:
            p1 = p1.next
        
        if p2 is None:
            p2 = headA
        else:
            p2 = p2.next
            
    return p1
