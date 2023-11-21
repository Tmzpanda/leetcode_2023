def reverse(x: int) -> int:
    res = -int(str(x)[::-1].strip('-')) if x < 0 else int(str(x)[::-1])
    return res if res in range(-2**31, 2**31) else 0

def reverse(self, x: int) -> int:
    MIN = -2**31
    MAX = 2**31 - 1

    res = 0
    while x:
        x, remainder = int(x/10), int(math.fmod(x, 10))
        if (res > MAX//10) or (res == MAX//10 and remainder >= MAX%10):
            return 0
        if (res < MIN//10) or (res == MIN//10 and remainder <= MIN%10):
            return 0

        res = res*10 + remainder

    return res

