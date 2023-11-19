def removeKdigits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while stack and stack[-1] > digit and k:    # non-decreasing
            stack.pop()
            k -= 1
        stack.append(digit)
    
    res = stack[:-k] if k else stack
    return "".join(res).lstrip('0') or "0"
        
