def lowestCommonAncestor(p: 'Node', q: 'Node') -> 'Node':
    visited = set()
    while p:
        visited.add(p.val)
        p = p.parent

    while q:
        if q.val in visited: 
            return q
        visited.add(q.val)
        q = q.parent
        
    return None
