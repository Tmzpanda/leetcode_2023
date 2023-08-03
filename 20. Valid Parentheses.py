def isValid(s: str) -> bool:
    stack = []
    mapping = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for char in s:
        if char in mapping:
            stack.append(char)
        else:
            if not stack or char != mapping[stack.pop()]:
                return False
            
    return not stack
