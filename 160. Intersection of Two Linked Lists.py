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
