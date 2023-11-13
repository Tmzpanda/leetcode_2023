# 2-(3+4)
def calculate(s: str) -> int:    
    stack = []
    pre_op = 1
    num = 0
    csum = 0

    for c in s+'+':
        if c.isdigit():
            num = num*10 + int(c)
        elif c in '+-':
            csum += pre_op * num
            pre_op = -1 if c == '-' else 1                      
            num = 0 
        elif c == '(':
            stack.append((csum, pre_op))
            csum, pre_op = 0, 1
        elif c == ')':
            csum += pre_op*num
            psum, pre_op = stack.pop()
            csum = psum + pre_op*csum
            num = 0

    return csum
