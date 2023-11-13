# 3+2*2
def calculate(s: str) -> int:
    stack = []
    pre_op = '+'
    num = 0
    for c in s+'+':
        if c.isdigit():
            num = num*10 + int(c)
            
        elif c in '+-*/':
            if pre_op == '+': stack.append(num)
            elif pre_op == '-': stack.append(-num)
            elif pre_op == '*': stack.append(stack.pop()*num)
            elif pre_op == '/': stack.append(math.trunc(stack.pop()/num))   # -3/2

            pre_op = c
            num = 0
            
    return sum(stack)
        
