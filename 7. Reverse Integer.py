def reverse(x: int) -> int:
    res = -int(str(x)[::-1].strip('-')) if x < 0 else int(str(x)[::-1])
    return res if res in range(-2**31, 2**31) else 0

