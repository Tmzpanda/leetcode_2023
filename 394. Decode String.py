def decodeString(s: str) -> str: 
    stack = []
    cstr = ""
    num = 0
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        if char.isalpha():
            cstr += char
        if char == '[':
            stack.append((cstr, num))
            cstr, num = "", 0
        if char == ']':
            pstr, pnum = stack.pop()
            cstr = pstr + pnum*cstr 

    return cstr
