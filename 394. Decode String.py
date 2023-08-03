def decodeString(s: str) -> str: 
    stack = []
    res = ""
    num = 0
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        if char.isalpha():
            res += char
        if char == '[':
            stack.append(res)
            stack.append(num)
            res = ""
            num = 0
        if char == ']':
            pnum = stack.pop()
            pstr = stack.pop()
            res = pstr + pnum*res

    return res
