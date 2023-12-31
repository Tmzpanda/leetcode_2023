# O(nlogk)
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # edge
    if not lists: 
        return None
    # base
    if len(lists) == 1:
        return lists[0]

    # d&q
    mid = len(lists) // 2
    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])
    return merge(left, right)
    
def merge(l1: ListNode, l2: ListNode) -> ListNode:
    cur = dummy = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    cur.next = l1 or l2
    return dummy.next 


# heap
from heapq import heappush, heappop

ListNode.__lt__ = lambda x, y: (x.val < y.val)

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    pred = dummy = ListNode(-1)
    
    heap = []
    for node in lists:
        if node:
            heappush(heap, node)

    while heap:
        node = heappop(heap)
        pred.next = node
        if node.next:
            heappush(heap, node.next)
        pred = node

    return dummy.next

