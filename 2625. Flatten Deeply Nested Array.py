# recursion
def flat(arr, n):
    res = []
    for item in arr:
        if isinstance(item, list) and n > 0:
            res.extend(flat(item, n - 1))
        else:
            res.append(item)
    return res


# stack
def flat(arr, n):
    res = []
    stack = [(item, n) for item in reversed(arr)]
    
    while stack:
        item, depth = stack.pop()
        if isinstance(item, list) and depth > 0:
            for sub_item in reversed(item):
                stack.append((sub_item, depth - 1))
        else:
            res.append(item)
            
    return res
