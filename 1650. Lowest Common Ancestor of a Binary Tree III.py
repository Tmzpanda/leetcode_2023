def lowestCommonAncestor(p: 'Node', q: 'Node') -> 'Node':
    visited = set()
    while p:
        visited.add(p.val)
        p = p.parent

    while q:
        if q.val in visited: 
            return q
        q = q.parent
        
    return None
